from urllib.robotparser import RobotFileParser
from crawlerlib.sitemap_interpreter import SitemapInterpreter
from os import mkdir, path, remove
from hashlib import sha1
from crawlerlib.rest_client import RestClient
from glob import glob
from lxml import etree
import gzip

def main():
    si = SitemapInterpreter('http://food.com')
    si.download_sitemaps()
    si.decompress_sitemaps()
    si.create_links_file()
    
if __name__ == '__main__':
    main()
