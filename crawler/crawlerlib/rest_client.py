from urllib.request import Request, urlopen, HTTPError

class RestClient(object):
    user_agent = 'chewigy-bot/1.0'

    def get(self, url):
        request = Request(url, None, headers={'User-agent': self.user_agent})
        response = urlopen(request)
        body = response.read()
        return body.decode("utf-8")
    