import random,string,xlrd,time,httpx,json
from aip import AipSpeech
from pydub import AudioSegment
from pydub.playback import play

APP_ID = '26137266'
API_KEY = 'GdxlX6EY5HUlx7NpxrXQQtfA'
SECRET_KEY = 'POBZkNlIkiwbI68QRuuEjs55OXfcpCMR'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_token():
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    res = httpx.post(token_url,data={
        'grant_type':'client_credentials',
        'client_id':'oW9rcZyBOkMSrUuULeN4IxCQ',
        'client_secret':'oa1TRIlxs5WjfZiUHh9Ej8e2e6rS15d5'
        })
    return res.json()['access_token']

def read():
    text_to_voice(translate(input("请输入初始语言"),input("请输入你要翻译的语言"),q = input('''
                ==========================================
                |      输入一个你要翻译的单词（句子）       |
                ==========================================
                | your input: ''')))
    
    
def translate(from_lang, to_lang, q):
    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : ''}

    # Send request
    url = f'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token={get_token()}'
    r = httpx.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    speak_sentence = result["result"]["trans_result"][0]["dst"]
    return speak_sentence

def text_to_voice(text):
    print(text)
    result  = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })
    text = text.replace(' ', '')
    if not isinstance(result, dict):
        with open('{}-result.mp3'.format(text), 'wb') as f:
            f.write(result)
        return play_voice('{}-result.mp3'.format(text))

def play_voice(file_input_path):
    #print(file_input_path)
    if file_input_path.endswith('.wav'):
        song = AudioSegment.from_wav(file_input_path)
    elif file_input_path.endswith('.mp3'):
        song = AudioSegment.from_mp3(file_input_path)
    #print(dir(song))
    if song != None:
        play(song)
    else:
        print('may be have something wrong?~')

if __name__ == '__main__':
    read()