from lxml import etree
from urllib.error import HTTPError
from urllib.robotparser import RobotFileParser
from crawlerlib.rest_client import RestClient
from crawlerlib.data_archiver import DataArchiver
from os import mkdir, path, remove
from glob import glob
from hashlib import sha1
import logging
import gzip
import hashlib

class SitemapInterpreter(object):
    def __init__(self, root_url):
        """
        Create and initialize a SitemapInterpreter given a ``root_url`` which does not end in a trailing slash.
        """
        self.sitemap_url = root_url + '/sitemap.xml'
    
    def fetch_urls(self, robot_parser):
        """
        Visit the sitemap and download outer sitemaps locations. Unzip them and return permitted urls in a list.

        Arguments:
            robot_parser: A urllib.robotparser to filter permitted sites.

        Returns:
            - Permitted urls as a list on Success
            - None in exceptional circumstances.
        """
        client = RestClient()
        try:
            response = client.get(self.sitemap_url).decode("utf-8")
        except HTTPError:
            logging.fatal('Could not reach sitemap.')
            return None
        xml = etree.XML(response)
        return xml.xpath('//*[local-name()="loc"]/text()')
    
    def download_sitemaps(self):
        """
        Download all gzipped sitemaps to the data/sitemaps directory.
        """
        client = RestClient()
        robotparser = RobotFileParser(url='http://food.com/robots.txt')
        urls = self.fetch_urls(robotparser)
        data_dir = 'data/'
        sitemaps_dir = data_dir + 'sitemaps'
        if not path.exists(data_dir):
            mkdir(data_dir)
        if not path.exists(sitemaps_dir):
            mkdir(sitemaps_dir)
        for url in urls:
            hash_name = sha1(str.encode(url)).hexdigest()
            body = client.get(url)
            f = open('data/sitemaps/{0}.tgz'.format(hash_name), 'wb')
            f.write(body)
            f.close()
    
    def decompress_sitemaps(self):
        """
        Unzip all of the sitemap files and delete the zipped versions.
        """
        for zipped_file_path in glob('data/sitemaps/*.tgz'):
            with gzip.open(zipped_file_path, 'rb') as inp:
                with open(zipped_file_path.replace('.tgz', '.xml'), 'wb') as out:
                    out.write(inp.read())
            remove(zipped_file_path)
    
    def create_links_file(self):
        """
        Create a data/LINKS file which has one recipe link per line.
        """
        with open('data/LINKS', 'w') as out:
            for xml_file_path in glob('data/sitemaps/*.xml'):
                xml = etree.parse(xml_file_path)
                for location in xml.xpath('//*[local-name()=\'loc\']/text()'):
                    if "food.com/recipe/" in location and not "/review" in location:
                        out.write(location + '\n')
                        print(location)