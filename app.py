import bomber
import asyncio

#Set Your inputs
input_keyword = "Marketing Automation"
input_country = "US"

#Set your Open AI API Key
API_KEY = "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"

print("strated.........")
#run
result =  asyncio.run(bomber.get_keyword_data(input_keyword,input_country,API_KEY))

print('ended..........')