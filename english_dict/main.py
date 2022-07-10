import xlrd,time,random
from wordle import wordle
from order import order
from find import find
from read_word import read
from repeat import main_repeat
from repeat import init_word_repeat

word_all = []
word_all_lower = []

def init_word():
    read_book = xlrd.open_workbook("人教版初中英语.xls")
    sheet = read_book.sheets()
    for sheet_num in range(0,len(sheet)):
        sheet = read_book.sheets()[sheet_num]
        for word_list in range(1,int(sheet.nrows)):
            is_phrase = False
            word_every = sheet.cell_value(word_list, 0)
            if not '.' in sheet.cell_value(word_list, 1):
                is_phrase = True
                word_all.append({'单词':word_every,'词性':'','中文':sheet.cell_value(word_list, 1)})
                word_all_lower.append({'单词':word_every.lower(),'词性':'','中文':sheet.cell_value(word_list, 1)})
            if is_phrase == False:
                a = sheet.cell_value(word_list, 1).split('.')
                word_all.append({'单词':word_every,'词性':a[0]+'.','中文':a[1]})
                word_all_lower.append({'单词':word_every.lower(),'词性':a[0]+'.','中文':a[1]})
    random.shuffle(word_all)

def main():
    init_word()
    while True:
        try:
            print("""
            ███████╗███╗   ██╗ ██████╗ ██╗     ██╗███████╗██╗  ██╗
            ██╔════╝████╗  ██║██╔════╝ ██║     ██║██╔════╝██║  ██║
            █████╗  ██╔██╗ ██║██║  ███╗██║     ██║███████╗███████║
            ██╔══╝  ██║╚██╗██║██║   ██║██║     ██║╚════██║██╔══██║
            ███████╗██║ ╚████║╚██████╔╝███████╗██║███████║██║  ██║
            ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝""")
            print("""
            ·▄▄▄▄  ▪   ▄▄· ▄▄▄▄▄▪         ▐ ▄  ▄▄▄· ▄▄▄   ▄· ▄▌
            ██▪ ██ ██ ▐█ ▌▪•██  ██ ▪     •█▌▐█▐█ ▀█ ▀▄ █·▐█▪██▌
            ▐█· ▐█▌▐█·██ ▄▄ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐█▌▐█▪
            ██. ██ ▐█▌▐███▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█ ▪▐▌▐█•█▌ ▐█▀·.
            ▀▀▀▀▀• ▀▀▀·▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀  ▀ .▀  ▀  ▀ • """)
            time.sleep(1)
            home_main = input('''
            ==============================================
                        可以用 ‘退出’ 二字退出哦
            ==============================================
            | 1 排序        |           |2 wordle        |
            |               |  welcome! |                |
            |   (顺序排列)   |    to     |   (长度选择)   |
            |      or       |    the    |      and       |
            |   (倒序排列)   |   Enlish  |   (完美复刻)   |
            |===============| dictionary|================|
            |3 查找         |    and    | 4 翻译朗读功能  |
            |               |  wordle   |                |
            |    (字母查找)  |           |      (百度)    |
            |       and     |   enjoy   |                |
            |    (长度查找)  |    it     |   (不要乱输哦)  |
            ==============================================
            | 5 记单词                                    |                                            
            |                                            |
            ==============================================
            |your input: ''')
            home_main_int = int(home_main)
            if home_main_int < 0 or home_main_int > 5:
                print('opps,try again')
                time.sleep(1)
            else:
                if home_main_int == 1:
                    order(word_all, word_all_lower)
                elif home_main_int == 2:
                    wordle(word_all)
                elif home_main_int == 3:
                    find(word_all)
                elif home_main_int == 4:
                    read()
                elif home_main_int == 5:
                    init_word_repeat()
                    main_repeat()
                
                
        except Exception as e:
            print(e)
            if home_main == '退出':
                print('bye!')
                time.sleep(1)
                break
            time.sleep(1)

if __name__ == '__main__':
    main()