import requests
from bs4 import BeautifulSoup as bs
#import scraper


url = 'https://www.kollegierneskontor.dk/default.aspx?func=kkikportal.login&lang=DK'


with requests.Session() as s:
    site = s.get(url)
    soup = bs(site.content, 'html.parser')

    login_data = {
        'Page$ctl08$Main$ctl04$form$loginUserName':'matthewkwakuwilson@gmail.com',
        'Page$ctl08$Main$ctl04$form$loginPassword':'2RYyRQN~V@N_!Qbm>R)D',
        '__VIEWSTATE':soup.find('input', id='__VIEWSTATE')['value'],
        '__VIEWSTATEGENERATOR':soup.find('input', id='__VIEWSTATEGENERATOR')['value'],
        '__EVENTVALIDATION':soup.find('input', id='__EVENTVALIDATION')['value']
    }
    request_headers = {
        'Host':'www.kollegierneskontor.dk',
        'Connection':'keep-alive',
        'Content-Length': '7215',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://www.kollegierneskontor.dk',
        'Upgrade-Insecure-Requests': 1,
        'DNT': 1,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User':'?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Referer': 'https://www.kollegierneskontor.dk/default.aspx?func=kkikportal.login&lang=DK',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie':s.cookies.values(),
    }
    print(request_headers)

    #r = s.post(url, data = login_data, headers = dict(referer = url))
#r = s.get('https://www.kollegierneskontor.dk/default.aspx?func=kkikportal.housingrequests&lang=DK')
    #print(r)

#scraper.saveData(scraper.getData(r.content))
