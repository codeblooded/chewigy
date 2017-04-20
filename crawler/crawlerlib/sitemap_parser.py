from lib.rest_client import RestClient
from urllib.error import HTTPError
import logging

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
            response = client.get(self.sitemap_url)
            return response
        except HTTPError:
            logging.fatal('Could not reach sitemap.')
            return None