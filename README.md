I have built this BhavCopy Web App using Django, python, redis, Pandas, HTML, CSS, CronJob

Description-->
This tool Downloads the Equity BhavCopy Zip  from the page. https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx.
Then it will Unzip it and store the data like CODE, NAME, OPEN, HIGH, LOW, CLOSE. And store into SQlite3 and store the cache into Redis.
And User can search the stock and the related data which was cached will provided to you in the form of a table.
You can also download the filtered data as a .csv format.

Working-->
This Web App UI consists of a input textbox where user need to enter the related stock name in equity.
The the request goes and check into the Redis Cache and if the data present it will give the data back. 
In case if the data is not present it will retrive it from the sqlite db an dset it into the Redis Cache
And then the resulted data is provided back to you in the form of tabular format.
You also have an option to download the tabular data into csv file.

