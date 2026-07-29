import os
from dotenv import load_dotenv
import requests
from datetime import datetime,timezone

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
        if change_percent>0:
            sign='+'
        else:
            sign=''
        prompt=f'''
Current Date: {datetime.now(timezone.utc)}
Company Name: {name}
Current Price: ${current_price}
Today's Change : {sign}${company_info['quote']['ChangeAmount']} ({sign}{change_percent}%)
Recent Articles (newest first):'''
        count=1
        for article in company_info['articles']:
            prompt+=f'\n{count}.\n{article['Name']}\nTitle: {article['Title']}\nPublished: {article['Published']}'
            count+=1
        prompt+='''
Task:
- Explain today's stock movement.
- Relate your explanation to the supplied articles.
- If the articles do not sufficiently explain the movement, explicitly say so.
- Do not speculate or invent causes.
- Keep the response under 150 words.
- Use clear, concise language suitable for an investor dashboard'''
        return prompt


    def get_gemini_explanation(self,company_info):
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



        
        
    