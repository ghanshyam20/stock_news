

import requests


STOCK_NAME="TSLA"





COMPANY_NAME="Tesla Inc"


STOCK_ENDPOINT="https://www.alphavantage.co/query"



#step 1 :use https://www.alphavantage.co/support/#api-key

#to get yesterdays closing price
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}

response=requests.get(STOCK_ENDPOINT,stock_params)

data=response.json()["Time Series (Daily)"]






#list compreshension
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)




#Get the day before yesterday's closing stock price 

day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)



#Finding the positive differene between step 1 and step 2
#python abs function


difference=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))

print(difference)

# work out on the percentage difference in price between closing price yesterday and closing price the day before yesterday

diff_percent=(difference/float(yesterday_closing_price))*100
print(diff_percent)


#if percentage is greater than 5 then print ("GET NEWS")


#if diff_percent>5:
 #   print("GET News")



#FOR THE NEWS OF STOCK UP AND DOWN 

#I used  https://newsapi.org/v2/everything FOR NEWSAPI END POINT

NEWS_ENDPOINT="https://newsapi.org/v2/everything"




if diff_percent>5:
    news_params={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }


    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json["articles"]


    three_articles=articles[:3]
    print(three_articles)





