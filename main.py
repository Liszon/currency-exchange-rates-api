#Liszewski Artur
#API-CRON-Backup
import json
import csv
import requests
import datetime
import restic

#url = 'http://api.exchangeratesapi.io/v1/latest?access_key=a30a9d42aef5f4bd4ebe4a98cb7e2a6a&symbols=USD,AUD,CAD,PLN'

APIKEY='a30a9d42aef5f4bd4ebe4a98cb7e2a6a'


today = datetime.date.today() #getting the current date
datelist = ['latest',"1","2","3","4","5","6"] #creating a list in which to place the dates
#filling in a list of dates
for i in range(1,7):
    day = today+datetime.timedelta(days=0-(i+1))
    day = day.strftime("%Y-%m-%d")
    datelist[i] = day

#a list containing all urls
urllist=['http://api.exchangeratesapi.io/v1/'+datelist[0]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN', 'http://api.exchangeratesapi.io/v1/'+datelist[1]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN', 'http://api.exchangeratesapi.io/v1/'+datelist[2]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN', 'http://api.exchangeratesapi.io/v1/'+datelist[3]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN', 'http://api.exchangeratesapi.io/v1/'+datelist[4]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN', 'http://api.exchangeratesapi.io/v1/'+datelist[5]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN', 'http://api.exchangeratesapi.io/v1/'+datelist[6]+'?access_key='+APIKEY+'&symbols=USD,AUD,CAD,PLN']

#reading data from individual URLs and saving them to separate lists

#Today
response = requests.get(urllist[0])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate0=[1,2,3,4]
currency0=[" "," "," "," "]
for currency, rate in rates.items():
    rate0[i] = rate
    currency0[i] = currency
    i=i+1

#Yesterday
response = requests.get(urllist[1])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate1=[1,2,3,4]
for currency, rate in rates.items():
    rate1[i] = rate
    i=i+1

#2 days ago
response = requests.get(urllist[2])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate2=[1,2,3,4]
for currency, rate in rates.items():
    rate2[i] = rate
    i=i+1

#3 days ago
response = requests.get(urllist[3])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate3=[1,2,3,4]
for currency, rate in rates.items():
    rate3[i] = rate
    i=i+1

#4 days ago
response = requests.get(urllist[4])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate4=[1,2,3,4]
for currency, rate in rates.items():
    rate4[i] = rate
    i=i+1

#5 days ago
response = requests.get(urllist[5])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate5=[1,2,3,4]
for currency, rate in rates.items():
    rate5[i] = rate
    i=i+1

#6 days ago
response = requests.get(urllist[6])
data = response.text
parsed = json.loads(data)
rates = parsed["rates"]
i=0
rate6=[1,2,3,4]
for currency, rate in rates.items():
    rate6[i] = rate
    i=i+1

#Saving the data in a CSV file
with open('currency.csv', 'w',newline='') as file:
    writer=csv.writer(file, delimiter=';')
    writer.writerow(["Currency", "Rate", "Yesterday", "2 days ago", "3 days ago", "4 days ago", "5 days ago", "6 days ago"])
    writer.writerow(["EUR", 1, 1, 1, 1, 1, 1, 1])
    for i in range(4):
        writer.writerow([currency0[i], rate0[i], rate1[i], rate2[i], rate3[i], rate4[i], rate5[i], rate6[i]])

#Creating backup
restic.repository = '/backup'
restic.password_file = 'password.txt'

try:
    restic.init()
    print("Creating backup")
except:
    print("Backup alredy exist")

restic.backup(paths=['currency.csv'])

restic.restore(snapshot_id='latest', target_dir='restored')