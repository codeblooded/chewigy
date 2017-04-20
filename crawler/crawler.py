from urllib.robotparser import RobotFileParser
from crawlerlib.sitemap_parser import SitemapParser
from os import mkdir, path, remove
from hashlib import sha1
from crawlerlib.rest_client import RestClient
from glob import glob
from lxml import etree
import gzip

def fetch_sitemaps():
    client = RestClient()
    robotparser = RobotFileParser(url='http://food.com/robots.txt')
    foodComSitemap = SitemapParser('http://food.com')
    urls = foodComSitemap.fetch_urls(robotparser)
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

def decompress_sitemaps():
    for zipped_file_path in glob('data/sitemaps/*.tgz'):
        with gzip.open(zipped_file_path, 'rb') as inp:
            with open(zipped_file_path.replace('.tgz', '.xml'), 'wb') as out:
                out.write(inp.read())
        remove(zipped_file_path)

def get_routes():
    with open('data/LINKS', 'w') as out:
        for xml_file_path in glob('data/sitemaps/*.xml'):
            xml = etree.parse(xml_file_path)
            for location in xml.xpath('//*[local-name()=\'loc\']/text()'):
                out.write(location + '\n')

def main():
    # fetch_sitemaps()
    # decompress_sitemaps()
    get_routes()
    
if __name__ == '__main__':
    main()
