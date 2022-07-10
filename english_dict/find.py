import time

def find(word_all):
    answer = input('''
        =======================
        |   1.按首字母查询     |
        =======================
        |   2.包含字母就查询   |
        =======================
        |   3.长度查找        |
        =======================
        |   4.退出            |
        =======================
        |your input: ''')
    if answer == '1':
        word_first_letter = input('''
                  输入你想要的首字母
            ===========================
            |your input: ''')
        word_list_right = []
        for every_word in word_all:
            find_word_head_letter = every_word['单词']
            if find_word_head_letter[0] == word_first_letter:
                word_list_right.append(every_word)
        for numbers in range(0,len(word_list_right),10):
            for order_show in range(numbers,numbers+10):
                    print(word_list_right[order_show])
                    time.sleep(0.001)
            answer_second = input('''
                ====================
                |      下一页?      |
                |    (yes or no)   |
                |===================
                |your input: ''')
            if answer_second == 'yes':
                continue
            else:
                break
    if answer == '2':
        word_first_letter = input('''
                  输入你想要的包含字母
            ===========================
            |your input: ''')
        word_list_right = []
        for every_word in word_all:
            find_word_head_letter = every_word['单词']
            for every_letter in range(0,len(find_word_head_letter)):
                if find_word_head_letter[every_letter] == word_first_letter:
                    word_list_right.append(every_word)
        for numbers in range(0,len(word_list_right),10):
            for order_show in range(numbers,numbers+10):
                    print(word_list_right[order_show])
                    time.sleep(0.001)
            answer_second = input('''
                ====================
                |      下一页?      |
                |    (yes or no)   |
                |===================
                |your input: ''')
            if answer_second == 'yes':
                continue
            else:
                break
    if answer == '3':
        letter_length = input('''
            =============================
                输入你想要查找的单词长度
            =============================
            |your input: ''')
        if letter_length.isdigit():
            letter_length = int(letter_length)
            filter_words = [w for w in word_all if len(w['单词']) == letter_length]
            for numbers in range(0,len(filter_words),10):
                for order_show in range(numbers,numbers+10):
                        print(filter_words[order_show])
                        time.sleep(0.001)
                answer_second = input('''
                    ====================
                    |      下一页?      |
                    |    (yes or no)   |
                    |===================
                    |your input: ''')
                if answer_second == 'yes':
                    continue
                else:
                    break
        else:
            print('Your input is not a number')
    a = []
    myList = word_all_copy
    for i in myList:
        myList1 = sorted(i.values,key = lambda i:len(i),reverse=True) 
        a.append(myList1)
    print(a)