import requests
import random
import json
token = '24.5b7683341c8b7df4b41154bff5035a2d.2592000.1659576634.282335-26285995'
url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

def fy():
        q = input('输入:'); # example: hello
        # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
        from_lang = 'wyw'; # example: en
        to_lang = 'zh'; # example: zh
        term_ids = ''; #术语库id，多个逗号隔开
        
        # Build request
        headers = {'Content-Type': 'application/json'}
        payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

        # Send request
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
	
        # Show response
        print(result["result"]["trans_result"][0]["dst"])
if __name__ == "__main__":
        fy()


def fyl(next_sentence):
		# example: hello
        # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
        from_lang = 'wyw'; # example: en
        to_lang = 'zh'; # example: zh
        term_ids = ''; #术语库id，多个逗号隔开
        
        # Build request
        headers = {'Content-Type': 'application/json'}
        payload = {'q': next_sentence, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

        # Send request
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
	
        # Show response
        print(result["result"]["trans_result"][0]["dst"])
if __name__ == "__main__":
        fyl()
                        
                 
