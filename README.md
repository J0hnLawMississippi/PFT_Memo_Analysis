# PFT_Memo_Analysis

We extract Memos of Postfiat (PFT) token transactions on the XRP blockchain and rank the associated network users with Mistral & OpenAI models.
Users that have generated data on the blockchain receive scores in different categories to assess their overall likelihood of understanding NVDA stock.

minimal requirements:

Python 3.11

asyncio 3.4.3

aiohttp 3.11.10

json 2.09

xrpl-py 3.0.0

async_token_memos.py gets the PFT token transactions with xrpl-py, extracts memo-data and writes the result to the full_memo_data json file.

memo_scores.py reads in memo data, filters the data for users and runs a gpt-4o or mistral-large prompt via openrouter to classify users by their expertise in different categories.
Score weight categories can be adapted in the prompt to generate different results and check them for convergence or lack thereof. A final AI model weighted score ouput is generated for each network user.

single_user_scores.py queries memo data for a single user and outputs an explanation for scores, every score component, a human as well as an AI weighted score.

post_processing.py reads in the user scores and ouputs the top30 users for a given set of results.
