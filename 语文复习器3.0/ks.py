from aip import AipSpeech
from playsound import playsound

""" 你的 APPID AK SK """
APP_ID = "26635464"
API_KEY = 'OjPx3GzwLzCVCF1FyAjMZFhN'
SECRET_KEY = 'njg3SBQ0I8vLCSHy512q8X4GayiZIFY4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def yp(next_sentence):
    result  = client.synthesis(next_sentence, 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    else:
        print(result)
    playsound('audio.mp3')
