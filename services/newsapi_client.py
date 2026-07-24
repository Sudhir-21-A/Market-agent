import os
from dotenv import load_dotenv
import requests
from datetime import datetime,timezone

load_dotenv()


class NewsApiClient():
    def __init__(self):
        self.base_url="https://newsapi.org/v2/everything"
        self.api_key=os.getenv("NEWS_API_KEY")


    def get_news(self,company_name):
        url=self.base_url
        params={
            "q":company_name,
            "searchIn":"title,description",
            "language": "en",
            "sortBy":"publishedAt",
            "pageSize":5,
            "page":1,
            "apikey":self.api_key
        }
        response=requests.get(url,params=params)
        articles=response.json()


        if articles is None:
            print(response.url)
            print(f'Status: {response.status_code}')
            return None

        if articles['status']=="error":
            print(f'Message: {articles['message']}')
            return None

        news_articles=articles['articles']
        final_articles=[]
        count=0
        for article in news_articles:
            count+=1
            new_article={}
            new_article['Number']=count
            new_article['Name']=article['source']['name']
            new_article['Author']=article['author']
            new_article['Title']=article['title']
            new_article['Url']=article['url']
            new_article['Description']=article['description']
            new_article['Content']=article['content']
            new_article['Published']=self.get_published_time(article['publishedAt'])
            final_articles.append(new_article)

        return final_articles


    def get_published_time(self,timestamp):
        time=datetime.strptime(
            timestamp,"%Y-%m-%dT%H:%M:%SZ"
        ).replace(tzinfo=timezone.utc)

        current_time=datetime.now(timezone.utc)
        diff=current_time-time

        seconds=diff.total_seconds()

        if seconds<60:
            time_response="Just Now"
        elif seconds<3600:
            if int(seconds//60)==1:
                time_response="1 min ago"
            else:
                time_response=f"{int(seconds//60)} mins ago"
        elif seconds<86400:
            if int(seconds//3600)==1:
                time_response="1 hr ago"
            else:
                time_response=f"{int(seconds//3600)} hrs ago"
        elif seconds<604800:
            if diff.days==1:
                time_response="1 day ago"
            else:
                time_response=f"{diff.days} days ago"
        else:
            time_response=time.strftime("%d %b %y")

        return time_response
        




        