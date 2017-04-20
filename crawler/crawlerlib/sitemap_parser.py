from lxml import etree
from urllib.error import HTTPError
from crawlerlib.rest_client import RestClient
from crawlerlib.data_archiver import DataArchiver
import logging
import gzip
import hashlib
import os

class SitemapParser(object):
    def __init__(self, root_url):
        """
        Create and initialize a SitemapParser given a ``root_url`` which does not end in a trailing slash.
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