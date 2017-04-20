from urllib.robotparser import RobotFileParser
from crawlerlib.sitemap_parser import SitemapParser

def main():
    robotparser = RobotFileParser(url='http://food.com/robots.txt')
    foodComSitemap = SitemapParser('http://food.com')
    urls = foodComSitemap.fetch_urls(robotparser)
    print(urls)

if __name__ == '__main__':
    main()
