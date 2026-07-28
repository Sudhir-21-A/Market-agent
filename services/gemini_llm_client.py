import os
from dotenv import load_dotenv
import requests

load_dotenv()

class GeminiClient():
    def __init__(self):
        self.api_key=os.getenv("GEMINI_API_KEY")
        self.base_url="https://generativelanguage.googleapis.com/v1beta/interactions"
        self.generation_config={
                                'max_output_tokens':300,
                                'thinking_level':'minimal',
                                'thinking_summaries':'none',
        }

    def get_llm_response(self,headers,json):
        # print('\nRequesting...')
        try:
            response=requests.post(self.base_url,headers=headers,json=json)
            response.raise_for_status()
            response_text=response.json()
            explanation=self.extract_explanation(response_text)
            return explanation
        except requests.exceptions.RequestException as e:
            print(e)
            return None


    def get_prompt(self,company_info):
        name=company_info['overview']['Name']
        current_price=company_info['quote']['CurrentPrice']
        change_percent=company_info['quote']['ChangePercent']
        prompt=f'''
Company Name: {name}
Current Price: {current_price}
Today's Change Percentage: {change_percent}%
Articles:'''
        count=1
        for article in company_info['articles']:
            prompt+=f'\n{count}. {article['Title']}'
            count+=1
        prompt+='''
You are a financial assistant.
Only use the supplied information.
Explain the stock movement in no more than 150 words.
Do not speculate.'''
        return prompt


    def get_gemini_explanation(self,company_info):
        # print("Getting prompt...\n")
        prompt=self.get_prompt(company_info)
        headers={
                'Content-Type': "application/json",
                'x-goog-api-key':self.api_key
        }
        json={
                'model':"gemini-3.6-flash",
                'input':prompt,
                'generation_config':self.generation_config
        }
        explanation=self.get_llm_response(headers,json)
        if explanation is None:
            return None
        return explanation



    def extract_explanation(self,response):
        steps=response['steps']
        for step in steps:
                if step['type']=='model_output':
                    explanation=step['content'][0]['text']
        return explanation



        
        
    