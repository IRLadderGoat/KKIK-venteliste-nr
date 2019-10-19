#A scraper that scrapes the names of posts on reddit and  their links

#https://www.reddit.com/r/SurfaceLinux/

#import requests
from bs4 import BeautifulSoup
import os
import csv

#Sets local url if nothing else has been set
#url = r'/home/matthew/Documents/git-repos/webscraperpy/kk.html'

#Gathers data from a determined URL
def getData(url):
    list_rentals = []
    list_wait_list_number = []

    #Utilizes bs4 to get html from page
    soup = BeautifulSoup(url, 'html.parser')

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


