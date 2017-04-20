from urllib.robotparser import RobotFileParser
from crawlerlib.sitemap_parser import SitemapParser

def main():
    robotparser = RobotFileParser(url='http://food.com/robots.txt')
    foodComSitemap = SitemapParser('http://food.com')
    urls = foodComSitemap.fetch_urls(robotparser)
    print(urls)

# def get(url):
#     request = Request(url, None, headers={'User-agent': 'chewigy-bot/1.0'})
#     response = urlopen(request)
#     try:
#         return response.read().decode("utf-8")
#     except HTTPError:
#         return None


# def create_data_directory():
#     """
#     Create a data directory and a subdirectory for today's crawl. Return the
#     subdirectory, so other files can be stored inside.

#     The directories are created relative to the present directory:
#     - data/
#     - data/TIMESTAMP/
#     """
#     root_data_dir = getcwd() + '/data'
#     today = datetime.now().strftime("%m_%d_%y__%H_%M_%S")
#     today_data_dir = '{0}/{1}'.format(root_data_dir, today)

#     if not path.exists(root_data_dir):
#         mkdir(getcwd() + '/data/')

#     if not path.exists(today_data_dir):
#         mkdir(today_data_dir)
    
#     return today_data_dir

# def get_site_maps(url):
#     """
#     Get the XML sitemap given a base url.
#     """
#     create_data_directory()
#     response = get(url + "/sitemap.xml")
#     sitemap = minidom.parseString(response)
#     return sitemap.getElementsByTagName('loc')

if __name__ == '__main__':
    main()
