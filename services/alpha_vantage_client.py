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
        if response.status_code==200:
            return response.json()

        print(f'Error {response.status_code}')
        return None
    
    def _is_valid(self,data):
        
        if data is None:
            return False

        if not data:
            return False
        
        if "Error Message" in data:
            return False
        
        return True
    
    def get_company_overview(self,symbol):
        data= self.make_request("OVERVIEW",symbol)

        if not self._is_valid(data):
            return None
        
        return data

    
    def get_global_quote(self,symbol):
        data=self.make_request("GLOBAL_QUOTE",symbol)
        
        if not self._is_valid(data):
            return None
        
        return data['Global Quote']







