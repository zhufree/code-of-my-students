import time

def order_one(list_a,reverse):
    order_reverse = sorted(list_a, key = lambda e:e.__getitem__('单词'),reverse = reverse)
    for number_of_pages in range(0,len(order_reverse),10):
        for order_show in range(number_of_pages,number_of_pages+10):
            print(order_reverse[order_show])
            time.sleep(0.001)
        ask_order = input('''
                 ======================
                 |下一页？（yes or no）|
                 ======================
                 | your input: ''')
        if ask_order == 'yes':
            continue
        else:
            break

def order(word_all, word_all_lower):
    while 1:
        order_request = input('''
                =============================
                |  1.顺序排列（区分大小写）   |
                |---------------------------|
                |  2.倒序排列（区分大小写）   |
                |---------------------------|
                |  3.顺序排列（不区分大小写） |
                |---------------------------|
                |  4.倒序排列（不区分大小写） |
                |---------------------------|
                |  5.返回                   |
                ============================
                |your input: ''')
        if order_request == '1':
            order_one(word_all,False)
        elif order_request == '2':
            order_one(word_all,True)
        elif order_request == '3':
            order_one(word_all_lower,True)
        elif order_request == '4':
            order_one(word_all_lower,False)
        elif order_request == '5':
            break
        else:
            print('oops,may be it is finish,so u can try again?')