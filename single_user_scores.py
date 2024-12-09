#!/usr/bin/env python3


import aiohttp
import asyncio
import json

#additional func args to be implemented openai/gpt-4o-2024-11-20
async def analyze_json_file(file_path, api_key, prompt, user): 
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
    
        filtered_data = [item for item in json_data if item['user'] == user]

        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openai/gpt-4o-2024-11-20", #"mistralai/mistral-large-2411", #set to model chosen in func arg
            "messages": [
                {"role": "system", "content":
                "You are a professional analyst classifying JSON data by actionable market intelligence."
                 },
                {"role": "user", "content": f"Analyze this JSON data:\n{json.dumps(filtered_data, indent=2)}\n\n{prompt}"}
            ]
        }

        

        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                result = await response.json()
                return result['choices'][0]['message']['content']
            else:
                return f"Error: {response.status}, {await response.text()}"


            
async def main():

    
    
    
    file_path = "/home/trademachine/PFT/full_memo_data0.json"
    api_key = "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"
    prompt = """Rank the 'data' content of the provided json by the likelihood that the associated 'user'
    has an understanding of NVDA stock with scores from a minimum of 0 to a maximum of 100.
    A score of 0 means 0% probability of understanding NVDA stock,
    a score of 100 means certainty of understanding NVDA stock.
    Rank the user in the following categories with scores from 0 to 100 in each:

    1. STOCK: NVDA stock specific knowledge;
    2. DOMAIN: broad knowledge of NVDA market sector and NVDA competitors in hardware, computing, semiconductors, AI
    and knowledge of tech stocks and Nasdaq in general;
    3. PRODUCT: specific knowledge about NVDA products like GPUs for AI or gaming, SoCs for mobile computing or
    the automotive market;
    4. AI: artificial intelligence specific know-how like LLMs, data analytics & processing,
    different machine learning systems and algorithms,statistics etc.;
    5. TRADING/PM: know-how in generating trade signals and their execution in the market, mentions of active
    trading in NVDA or stocks in same sector or portfolio allocation to NVDA stock or sector;
    6. BUSINESS: general understanding of company balance sheets, earnings;
    7. HUMAN WEIGHTED SCORE: an overall user score based on the following weights for the individual components:
     0.2 STOCK, 0.15 DOMAIN, 0.1 PRODUCT, 0.2 AI, 0.25 TRADING/PM, 0.1 BUSINESS;                                     
    8. MODEL WEIGHTED SCORE: an overall user score based on your own weights of the categories STOCK, DOMAIN,        
    PRODUCT,TRADING/PORTFOLIO MANAGEMENT,BUSINESS. In assigning your weights follow these guidelines:                
    Specific expertise is more valuable than broad expertise. Expertise with a direct link to economic utility       
    is more valuable than purely abstract/theoretical knowledge.            

    
    Format your response in 10 parts of pipe delimited blocks without providing calculation details:
    
    
    | <USERNAME> | 
    |Explanation: | <3-4 sentences providing reasoning for your scores and difference of human vs. model score weights>|,
    |STOCK: | <an integer from 0 to 100> |, 
    |DOMAIN: | <an integer from 0 to 100> |, 
    |PRODUCT: | <an integer from 0 to 100> |, 
    |AI: | <an integer from 0 to 100> |, 
    |TRADING/PM: | | <an integer from 0 to 100> |, 
    |BUSINESS: | | <an integer from 0 to 100> |, 
    |HUMAN WEIGHTED SCORE: | <an integer from 0 to 100> |, 
    |MODEL WEIGHTED SCORE: | <an integer from 0 to 100> | 
    
    """
    
    
    ##
    #leave AI out of score metric or reformulate to avoid biased weighting??
    #add score for derivatives in general, options on NVDA in particular??
    ##
    

    user = 'xgudvibes'

    result =  await analyze_json_file(file_path, api_key, prompt, user)
    print(result)
    
    
    
asyncio.run(main())









#make sure we get memos of ALL PFT transactions
#make sure we get ALL memos
#make sure we get ALL the right MemoData


#SCORE HOW WELL USERS UNDERSTAND NVDA
#1) equity know how
#2) stock specific know how
#3) GPUs
#4) AI market hardware
#5) gaming??
#6) tech stocks
#7) nasdaq
#8) NVDA options
#9) options
#10) anomalous options activity etc.

#categories
#1)stock specific
#2)domain specific
#3)tech specific GPUs (can be contraindication)
#4)adjacent domain
# 






