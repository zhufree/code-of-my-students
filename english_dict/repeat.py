import xlrd,random
from xlutils.copy import copy
def join(correct_1,correct_2,answer):
    if correct_2:
        if correct_1:
            print("你真棒")
            answer['熟练程度'] += 1
        else:
            print("很不幸")
    else:
        print(f'词性是：{answer["词性"]},中文是：{answer["中文"]}')
    answer['背诵次数'] += 1
    old_excel = xlrd.open_workbook('new_test_1.xls', formatting_info=True)
    new_excel = copy(old_excel)
    number_sheet = len(old_excel.sheets())
    old_sheet = old_excel.sheets()
    for II in range(number_sheet):
        ws = new_excel.get_sheet(II)
        rs = old_excel.sheets()[II]
        for j in range(1,old_sheet[II].nrows):
            # print(rs.cell_value(j,0),answer['单词'])
            if rs.cell_value(j,0) == answer['单词']:
                #print("加入成功")
                #print(II,j)
                ws.write(j, 3, answer['背诵次数'])
                if correct_1:
                    ws.write(j, 2, answer['熟练程度'])
    new_excel.save('new_test_1.xls')
    if correct_1:
        print('熟练程度已加1')
    print('背诵次数已加1')
def init_repeat():
    old_excel = xlrd.open_workbook('人教版初中英语.xls', formatting_info=True)
    new_excel = copy(old_excel)
    number_sheet = len(old_excel.sheets())
    old_sheet = old_excel.sheets()
    for i in range(number_sheet):
        ws = new_excel.get_sheet(i)
        for j in range(1,old_sheet[i].nrows):
            ws.write(j, 2, 0)#掌握程度（0：是新的，1：半新的；2是熟透的）
            ws.write(j, 3, 0)#次数
    new_excel.save('new_test_1.xls')
def main_repeat():
    while True:
        a = input('''
              =========================
              |1.初始化(重置)          |
              =========================
              |2.开始背单词            |            
              =========================
              |your input: '''
              )
        if a == "1":
            init_repeat()
        elif a == '2':
            b = input('''
              =========================
              |1.新单词                |
              =========================
              |2.温顾旧单词            |
              =========================
              |3.查询                  |
              =========================
              |your input:
              ''')
            if b == "1":
                new_word()
            elif b == '2':
                c = input('''
              =========================
              |1.第一次(无熟练度)       |
              =========================
              |2.第二次(初级熟练度)     |
              =========================
              |3.第三次(满级熟练度)     |
              =========================
              |your input:
             ''')
                if c == "1":
                    old_word_1()
                elif c == '2':
                    old_word_2()
                elif c == '3':
                    old_word_3()
            elif b == '3':
                slcd= input('你要查找熟练度为几的单词？(0~2)')
                a = [i for i in repeat_word_all if i['熟练程度'] == slcd and i['背诵次数'] >= 1]
                for x in(a):
                    print(f'单词：{x["单词"]},词性：{x["词性"]},中文：{x["中文"]},熟练程度：{x["熟练程度"]},背诵次数：{x["背诵次数"]}' )
        else:
            print('输入错误，请重新输入')
def new_word():
    while True:
        a = [i for i in repeat_word_all if i['背诵次数'] == 0]
        answer = random.choice(a)
        print(answer['单词'])  
        host_choice = input('''
            ========================================
            |是否会背这个单词？（yes or no or quit） |
            |======================================|
            |your input：
             ''')
        if host_choice == 'yes':
            join(True,False,answer)
            continue
        elif host_choice == 'no':
            join(False,False,answer)
            continue
        elif host_choice == 'quit':
            break
def old_word_1():
    while True:
        a = [i for i in repeat_word_all if i['熟练程度'] == 0 and i['背诵次数'] >=1]
        answer = random.choice(a)
        print(answer['单词'])
        host_choice = input('''
                =======================================
                |是否会背这个单词？（yes or no or quit）|
                |=====================================|
                |your input：
                 ''')
        if host_choice == 'yes':
            input('''
            ==================================
            |请说出这个单词的词性和中文         |
            ==================================
            |your input:''')
            print(f'词性：{answer["词性"]},中文：{answer["中文"]}' )
            host_answer = input('''
            ============================
            |请问你答对了吗？(yes or no)|
            |===========================
            |your input：
            ''')
            if host_answer == 'yes':
                join(True,True,answer)
                continue
            elif host_answer == 'no':
                join(False,True,answer)
                continue
        elif host_choice == 'no':
            join(False,False,answer)
            continue
        elif host_choice == 'quit':
            break




def old_word_2():
    while True:
        a = [i for i in repeat_word_all if i['熟练程度'] == 1 and i['背诵次数'] >=1]
        answer = random.choice(a)
        print(answer['单词'])
        host_choice = input('''
                =======================================
                |是否会背这个单词？（yes or no or quit）|
                =======================================
                |your input：''')
        if host_choice == 'yes':
            input('''
            ==================================
            |请说出这个单词的词性和中文         |
            ==================================
            |your input:''')
            print(f'词性：{answer["词性"]},中文：{answer["中文"]}' )
            host_answer = input('''
            =============================
            |请问你答对了吗？(yes or no) |
            =============================
            |your input:''')
            if host_answer == 'yes':
                join(True,True,answer)
                continue
            elif host_answer == 'no':
                join(False,True,answer)
                continue
        elif host_choice == 'no':
            join(False,False,answer)
            continue
        elif host_choice == 'quit':
            break

def old_word_3():
    while True:
        a = [i for i in repeat_word_all if i['熟练程度'] >= 2 and i['背诵次数'] >=1]
        answer = random.choice(a)
        print(answer['单词'])
        host_choice = input('''
                =======================================
                |是否会背这个单词？（yes or no or quit）|
                =======================================
                |your input：
                 ''')
        if host_choice == 'yes':
            input('''
            ===========================
            |请说出这个单词的词性和中文 |
            |==========================
            |your input:''')
            print(f'词性：{answer["词性"]},中文：{answer["中文"]}' )
            host_answer = input('''
            ============================
            |请问你答对了吗？(yes or no)|
            |===========================
            |your input:''')
            if host_answer == 'yes':
                join(True,True,answer)
                continue
            elif host_answer == 'no':
                
                continue
        elif host_choice == 'no':
            join(False,False,answer)
            continue
        elif host_choice == 'quit':
            break

repeat_word_all = []
def init_word_repeat():
    read_book = xlrd.open_workbook("new_test_1.xls")
    sheet = read_book.sheets()
    for sheet_num in range(0,len(sheet)):
        sheet = read_book.sheets()[sheet_num]
        for word_list in range(1,int(sheet.nrows)):
            is_phrase = False
            word_every = sheet.cell_value(word_list, 0)
            if not '.' in sheet.cell_value(word_list, 1):
                is_phrase = True
                repeat_word_all.append({'单词':word_every,'词性':'','中文':sheet.cell_value(word_list, 1) \
                    ,'熟练程度':int(sheet.cell_value(word_list, 2)),'背诵次数':int(sheet.cell_value(word_list, 3))})
            if is_phrase == False:
                a = sheet.cell_value(word_list, 1).split('.')
                repeat_word_all.append({'单词':word_every,'词性':a[0]+'.','中文':a[1],'熟练程度':int(sheet.cell_value(word_list, 2)),'背诵次数':int(sheet.cell_value(word_list, 3))})