from urllib.robotparser import RobotFileParser
from crawlerlib.sitemap_interpreter import SitemapInterpreter
from os import mkdir, path, remove
from hashlib import sha1
from crawlerlib.rest_client import RestClient
from glob import glob
from lxml import etree
import gzip
import logging

def main():
    si = SitemapInterpreter('http://food.com')
    logger = logging.getLogger('crawler')
    logger.info("Downloading sitemap files for food.com...")
    si.download_sitemaps()
    logger.info("Decompressing sitemap files...")
    si.decompress_sitemaps()
    logger.info("Extracting Links from decompressed sitemaps...")
    si.create_links_file()
    
if __name__ == '__main__':
    main()
