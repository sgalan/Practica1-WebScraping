#!/usr/bin/python

import sys, getopt
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import random

def delay() -> None:
    time.sleep(random.uniform(15, 30))
    return None

header_dict = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9,ca;q=0.8,en;q=0.7,nl;q=0.6",
    "Host": "httpbin.org",
    "Referer": "https://www.scraperapi.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5f93b147-070a862577ae5966438af607"}


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('get_nuts.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('get_nuts.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('Input file is: ', inputfile)
    print('Output file is: ', outputfile)

    # Load input dataframe
    df = pd.read_csv(inputfile, low_memory=False)

    # Enter to different html to extract NUTS3 code and store it
    for index, row in df.iterrows(): # iterate through the rows
        html = 'http://'+str(row['TED_NOTICE_URL'])
        try:
            page = requests.get(html, headers=header_dict)  # request access to the html
            soup = BeautifulSoup(page.content, features="lxml")  # get the content using BeautifulSoup
            # Look for the class containing NUTS
            nutscode = soup.find('span', class_ = 'nutsCode').contents[0].split()[0]
            df.loc[index, 'TAL_LOCATION_NUTS'] = nutscode  # Store NUTS3
            delay() # delay randomly from 15 to 30 seconds to avoid being blocked
        except:
            # sometimes this information is not available
            df.loc[index, 'TAL_LOCATION_NUTS'] = 'NA'
            delay()  # delay randomly from 15 to 30 seconds to avoid being blocked

    # Filter to keep only projects with NUTS complete and store output dataframe
    for p, i in df.iterrows():
        if len(str(i['TAL_LOCATION_NUTS'])) != 5:
            df.drop([p], inplace=True)

    df.to_csv(outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])

