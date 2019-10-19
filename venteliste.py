import os
import re
import csv
import requests
import argparse
import datetime as dt
from bs4 import BeautifulSoup as bs

def login_and_get(username,password):
    url = 'https://www.kollegierneskontor.dk/default.aspx?func=kkikportal.login&lang=DK'

    request_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    s = requests.Session()

    site = s.get(url)
    soup = bs(site.content, 'html.parser')
    # https://github.com/kraenhansen/findbolig.nu/blob/master/findbolig-venteliste-extractor.py
    data = dict()
    input_fields = re.findall('<input(.*)>', site.text, flags=re.IGNORECASE)
    for field in input_fields:
        name = re.findall('.*name="([^"]*)".*',field)
        value = re.findall('.*value="([^"]*)".*',field)
        typ = re.findall('.*type="([^"]*)".*',field)
        if typ[0] =='button':
            continue
        if name:
            if value:
                data[name[0]] = value[0]
            else:
                data[name[0]] = ""
    data['Page$ctl08$Main$ctl04$form$loginUserName'] = username
    data['Page$ctl08$Main$ctl04$form$loginPassword'] = password

    r = s.post(url, data = data, headers = request_headers, params = {'Referer': site.url})
    return r

def getData(url):
    list_rentals = []
    list_wait_list_number = []

    #Utilizes bs4 to get html from page
    soup = bs(url, 'html.parser')
    list_rentals.append('Date')
    list_wait_list_number.append(dt.datetime.now().date().isoformat())

    # Loops through the found rentals 
    for i in soup.find_all(class_='row header'):
        list_rentals.append(i.contents[7].get_text().strip())
        list_wait_list_number.append(i.contents[19].get_text().strip())
    return (list_rentals, list_wait_list_number)

def saveData(data_to_save):
    with open('data.csv', 'a') as csvFile:
        if os.stat('data.csv').st_size <= 0:
            head_writer = csv.DictWriter(csvFile, fieldnames=data_to_save[0])
            head_writer.writeheader()
            print("Wrote headers:", data_to_save[0])
        row_writer = csv.writer(csvFile)
        row_writer.writerow(data_to_save[1])
        csvFile.close()
    print("Wrote data:", data_to_save[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='KKIK Username', required=True)
    parser.add_argument('-p', '--password', help='KKIK Password', required=True)
    args = parser.parse_args()

    response = login_and_get(args.username,args.password)
    if 'Boligønsker' in response.text:
        saveData(getData(response.content))

