from django.shortcuts import render
import datetime, requests, zipfile, io, os, glob
import pandas as pd
from EquityListings.settings import BASE_DIR

from .models import Shares

# Create your views here.


def download_and_unzip(download_url, file_path):

    if not os.path.exists(file_path):
        resp = requests.get(download_url, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        })

        zname = file_path

        zfile = open(zname, 'wb')
        zfile.write(resp.content)
        zfile.close()

        with zipfile.ZipFile(zname, "r") as compressed_file:
            compressed_file.extractall(os.path.join(os.getcwd(), "data"))
    else:
        print("we have a cache ppresent locally")


def updateData(x):
    zip_file_url = 'https://www.bseindia.com/download/BhavCopy/Equity/'

    # name = "EQ190321"
    # file_name = "EQ190321_CSV.ZIP"
    # csv_file_name = name + ".csv"
    # folder_name = name + "_CSV"

    month = ('0' + str(x.month)) if len(str(x.month)) < 2 else str(x.month)

    name = "EQ" + str(x.day) + month + str(x.year)[2:]
    file_name = name + "_CSV.ZIP"
    csv_file_name = name + ".csv"
    folder_name = name + "_CSV"

    zip_file_url += file_name




    base_dir = BASE_DIR

    download_and_unzip(zip_file_url, file_path=os.path.join(base_dir, f'data\{file_name}'))

    data = pd.read_csv(os.path.join(base_dir, f'data\{csv_file_name}'))



    df = data[['SC_CODE', 'SC_NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']]


    filelist = glob.glob(os.path.join(os.path.join(base_dir,"data"), "*"))
    for f in filelist:
        os.remove(f)

    return df


def my_cron_job():
    for i in range(1):
        d = datetime.datetime.now()-datetime.timedelta(days = i+1)
        df = updateData(d)

        for _,data in df.iterrows():
            share = Shares(code = data['SC_CODE'],name = data['SC_NAME'], open = data['OPEN'], high=data['HIGH'], low = data['LOW'], close = data['CLOSE'])
            # share.code = data['SC_CODE']
            # share.name = data['SC_NAME']
            # share.open = data['OPEN']
            # share.high = data['HIGH']
            # share.low = data['LOW']
            # share.close = data['CLOSE']
            share.save()

        df = None
