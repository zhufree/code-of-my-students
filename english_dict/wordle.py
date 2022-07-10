import random,httpx,time

def wordle(word_all):
    print('''
        猜字符串游戏
        规则：输入你要猜的字符串长度，计算机会从初中英语词库中选一个单词。你可以输入符合这个长度初中英文单词来猜
        1. 如果你输入的字符串中的字母在目标字符串中并且位置也正确，计算机会在这一位显示√
        2. 如果字母正确，位置不对，计算机会在该字母位置显示-
        3. 如果目标字符串没有这个字母，计算机会显示x
        ''')
    while 1:
        word_length = int(input('请输入你要猜的字符串长度：'))
        if word_length == 1:
            print("找不到一个字母的单词，请重新输入长度")
            continue
        answer = ''
        fuhetiaojiandanci = [i['单词'] for i in word_all if len(i['单词']) == word_length]
        current_notice = []
        guess_frequency = 0
        guess_shengyucishu=0
        for i in range(word_length):
            current_notice.append('x')
        answer += random.choice(fuhetiaojiandanci)
        while 'x' in current_notice or '-' in current_notice:
            guess_word = input('请输入你猜的字符串: ')
            res = httpx.get(f'https://s3-us-west-2.amazonaws.com/words.alexmeub.com/otcwl2018/{guess_word}.json')
            if len(guess_word) != word_length:
                print('输入的字符串长度不正确')
            elif res.status_code == 404:
                print("请重新输入一个合法单词")
            else:
                for i, guess_letter in enumerate(guess_word):
                    if guess_letter == answer[i]:
                        current_notice[i] = '√'
                    elif guess_letter in answer:
                        current_notice[i] = '-'
                    else:
                        current_notice[i] = 'x'
                print(guess_word)
                print(' '.join(current_notice))
                guess_frequency +=1
                guess_shengyucishu =6-guess_frequency
                if guess_frequency == 6:
                    print("次数已用完，你输了")
                    print(f'答案:{answer}')
                    break
                else:
                    print(f'您已输入{guess_frequency}次，还有{guess_shengyucishu}次机会')
        print(f"""                                 
                               ============================
                                          游戏结束
                                        本次共用了{guess_frequency}次
                                    已超越全球99%的玩家
                               ============================
                        """)
        time.sleep(1)
        timmy_break = False
        while True:
            jixu=input('''
                               ============================
                                     请问要再玩一局吗？
                               1.继续游戏           2.我不玩了
                               ============================
                               |your input:''')
            if jixu == "1":
                break

            else:
                print('''
                               ============================
                                   谢谢游玩，欢迎下次继续
                               ============================
                ''')
                timmy_break = True
                break
        if timmy_break:
            break
                