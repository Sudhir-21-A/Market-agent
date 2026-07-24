import os
from dotenv import load_dotenv
import requests

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
            final_articles.append(new_article)

        return final_articles


        