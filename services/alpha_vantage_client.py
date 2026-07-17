import os
from dotenv import load_dotenv
import requests

load_dotenv()

class AlphaVantageClient():
    def __init__(self):
        self.api_key=os.getenv("ALPHA_VANTAGE_API_KEY")
        self.base_url="https://www.alphavantage.co/query"

    def make_request(self,function,symbol):
        params={
            "function":function,
            "symbol":symbol,
            "apikey":self.api_key
        }
        response=requests.get(self.base_url,params=params)
        print(response.url)
        if response.status_code==200:
            return response.json()

        print(f'Error {response.status_code}')
        return None
    
    def get_company_overview(self,symbol):
        return self.make_request("OVERVIEW",symbol)

    
    def get_global_quote(self,symbol):
        return self.make_request("GLOBAL_QUOTE",symbol)
    






