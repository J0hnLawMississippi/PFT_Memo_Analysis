#!/usr/bin/env python3

import asyncio
import json
from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models.requests import AccountTx
from xrpl.utils import hex_to_str

async def get_token_transaction_history(account, token_id):
    client = AsyncJsonRpcClient("https://s2.ripple.com:51234/")
    
    async def fetch_transactions(marker=None):
        request = AccountTx(
            account=account,
            limit=100000000,
            marker=marker
        )
        response = await client.request(request)
        return response.result
    
    all_transactions = []
    marker = None
    
    while True:
        result = await fetch_transactions(marker)
        transactions = result['transactions']
        
        for tx in transactions:

            #print(tx['tx_json'])
            if 'Memos' in tx['tx_json']: #and tx['tx']['TokenID'] == token_id:
                #print(tx['tx_json']['Memos'][0]['Memo'])
                all_transactions.append(tx['tx_json']['Memos'][0]['Memo'])
        
        #if 'marker' in result:
        #    marker = result['marker']
        else:
            break
    
    return all_transactions

async def main():
    account = "rnQUEEg8yyjrwk9FhyXpKavHyCRJM9BDMW"
    token_id = "PFT"
    
    memos = await get_token_transaction_history(account, token_id)

    memo_list = []

    for each in memos:
        #if all(hasattr(each, attr) for attr in ['MemoData','MemoFormat','MemoType']):
        #print(f"data: {hex_to_str(each['MemoData'])} ")
        #print(f"format: {hex_to_str(each['MemoFormat'])}")
        #print(f"type: {hex_to_str(each['MemoType'])}")
            memo_data = {
                "data": hex_to_str(each['MemoData']) if each.get('MemoData') else None,
                "user": hex_to_str(each['MemoFormat']) if each.get('MemoFormat')  else None,
                "task_timestamp": hex_to_str(each['MemoType']) if each.get('MemoType') else None
            }
            memo_list.append(memo_data)
        


    #print(memo_list)
    with open('full_memo_data0.json', 'w') as f:
        json.dump(memo_list, f)
        

        
    #print(memo_list)
    #for each in memo_list:

    
    
asyncio.run(main())



