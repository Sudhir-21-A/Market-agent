import os
from dotenv import load_dotenv
import requests

load_dotenv()



class FinnhubClient():
    def __init__(self):
        self.api_key=os.getenv("FINNHUB_API_KEY")
        self.base_url="https://finnhub.io/api/v1"

    
    def make_request(self,endpoint,symbol):
        url=self.base_url+endpoint
        params={
            'symbol':symbol,
            'token': self.api_key
        }
        response=requests.get(url,params=params)
        if response.status_code==200:
            data=response.json()
            return data
        
        print(f'Error:\nResponse:{response}\nStatus Code: {response.status_code}')
        print(response.url)
        return None
    

    def _is_valid(self,data):
        if data is None:
            return False
        
        if not data:
            return False
        
        return True
    

    def get_company_profile(self,symbol):
        company_profile=self.make_request("/stock/profile2",symbol)
        
        if not self._is_valid(company_profile):
            return None
        
        return {
                'Name': company_profile.get('name'),
                'Symbol':  company_profile.get('ticker'),
                'Country': company_profile.get('country'),
                'Industry': company_profile.get('finnhubIndustry'),
                'Website': company_profile.get('weburl'),
                'Logo': company_profile.get('logo'),
                'MarketCap': company_profile.get('marketCapitalization')
            }
    

    def get_quote(self,symbol):
        quote=self.make_request("/quote",symbol)

        if not self._is_valid(quote):
            return None
        
        return {
            'CurrentPrice': quote.get('c'),
            'ChangePercent': quote.get('dp')
        }
        
