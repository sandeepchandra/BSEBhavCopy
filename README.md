I have built this BhavCopy Web App using Django, Python, Redis, Pandas, HTML, CSS, CronJob

Description-->
This tool Downloads the Equity BhavCopy Zip  from the page. https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx.
Then it will Unzip it and store the data like CODE, NAME, OPEN, HIGH, LOW, CLOSE. And store into SQlite3 and store the cache into Redis.
And User can search the stock and the related data which was cached will provided to you in the form of a table.
You can also download the filtered data as a .csv format.

Working-->
This Web App UI consists of a input textbox where user need to enter the related stock name in equity.
The the request goes and check into the Redis Cache and if the data present it will provide the resultant data back. 
In case if the data is not present it will retrive it from the sqlite db and store it in Redis cache as well. So from the next time if you search with the same key it will get the data from Redis cache. As the redis will  store the data in key value pair.
And then the resulted data is provided back to you in the form of tabular format.
You also have an option to download the tabular data into csv file.


To run the Django Web App need to use below commands.

pip install -r requirements.txt   
python manage.py makemigrations   
python manage.py migrate    
python manage.py runserver    

To Go for the WebPage need to go to below path.

http://127.0.0.1:8000/Equity/


