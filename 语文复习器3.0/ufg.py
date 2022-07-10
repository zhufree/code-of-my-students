import xlrd
import random
import re
from ks import yp
from fy import fyl
read_book = xlrd.open_workbook("初中古诗文(1).xls")
poetry = {}
sheet = read_book.sheets()[0]
for i in range(0, 125):
    poetry[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1) 
titles = list(poetry.keys())
sentence = ''
next_sentence = ''

def new():
    global sentence
    global next_sentence
    title = random.choice(titles)
    print('------------------------')
    print("题目：",title)
    print('------------------------')
    content = poetry[title]
    content = re.sub(r'\(.*\)', '', content)
    sentence_list = re.split(r'[。，！？]', content)[:-1]
    sentence_list = [s.replace('\n', '') for s in sentence_list]
    sentence = random.choice(sentence_list)
    i = sentence_list.index(sentence)
    while i == len(sentence_list)-1:
        sentence = random.choice(sentence_list)
        i = sentence_list.index(sentence)
    next_sentence = sentence_list[i+1]
    sentence = re.sub(r'[《》！？；：“”‘’]', '', sentence)
    sentence = sentence.replace('\n', '').strip()
    print("上句：",sentence)
    print('------------------------')


def good():
    hello = input("答案要翻译按w，要读音按s，都要按d，都不要按z:")
    if hello == "w":
        print("--------------------------------")    
        fyl(next_sentence)
    elif hello == "s":
        yp(next_sentence)
    elif hello == "d":
        print("--------------------------------")  
        fyl(next_sentence)
        yp(next_sentence)
    elif hello == "z":
        pass
    else:
        print("输入有误，请重新输入")
def cs():
    print('''欢迎欢迎热烈欢迎，恭喜你，这位骚年，我们接下来要对你进行一场离了个大谱的测试，
如果你答对了十道题，我们就送你神秘大奖''')
    new()
    while True:
        ok = input('请说出下一句，或按a跳过:')
        
        while ok!= next_sentence:
            if ok=='a':
                new() 
                ok = input('请说出下一句，按a跳过，按b提示:')
                
            elif ok=='b':
                print("---------------------------------")
                print(next_sentence[:3]+'...?')
                print("---------------------------------")
                ok = input('请说出下一句，按a跳过，按b提示，按g显示答案:')
                print("======================================")
            elif ok=='g':
                print("答案：",next_sentence)
                print("""======================================""")
                good()
                new()
                ok = input('请说出下一句，按a跳过，按b提示:')
            else:
                if ok == "":
                    print("___________________________________________________")
                    ok = input('输入不能为空，请重新输入，按a跳过，按b提示，按g显示答案:')
                    print("___________________________________________________")
                else:
                    print("---------------------------------------------------")
                    ok = input("输入错误，请重新输入，按a跳过，按b提示，按g显示答案:")
                    print("---------------------------------------------------")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('恭喜你答对了，祝你在新的一年学业有成，虎虎生威')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
        good()
        print(".............................................")
        ok = input('是否还要继续？y继续n退出:')
        print(".............................................")
        if ok=='y':
            new()
        elif ok == "n":
            break 
        else:
            print("****************************")            
            print("输入错误")
            print("****************************")   
        
if __name__ == "__main__":
        cs()
