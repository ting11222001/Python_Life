#!/usr/bin/env python
# coding: utf-8

# In[1]:


def welcomepage():
    print('*'*50)
    print('{:=^44}'.format('歡迎使用備忘錄系統'))
    print('')
    print('1. 新增備忘錄')
    print('2. 顯示全部備忘錄')
    print('3. 查詢備忘錄')
    print('4. 輸出目前紀錄到您歷史備忘錄csv檔')
    print('5. 匯入您歷史備忘錄csv檔中')
    print('')
    print('0. 退出系統')
    print('*'*50)
    
memolist = []

def add_memo_dict():
    date = input('請輸入備忘錄日期：')
    content = input('請輸入備忘錄內容：')
    memodict = {'date': date,
                'content': content}
    memolist.append(memodict)
    print('新增' + date + '備忘錄完成！')

def show_memo_dict():
    if len(memolist) == 0:
        print('還沒有任何備忘錄!')
    else: 
        print('日期\t\t')
        for memo in memolist:
            print('{:s}\t\t'.format(memo['date']))
            
def search_memo_dict():
    searchdate = input('請輸入想要查詢的日期：')
    if len(memolist) == 0:
        print('還沒有任何備忘錄!')
    else: 
        print('日期\t\t\t備忘錄內容\t\t')
        for memo in memolist:
            if searchdate == memo['date']:
                print('{:s}\t\t{:s}\t\t'.format(searchdate, memo['content']))
                edit_delete_memo_dict(memo) 
                break
        else:
            print('沒有找到符合您輸入日期的備忘錄')
        
def edit_delete_memo_dict(memo):
    editoption = eval(input('請輸入想要對於此備忘錄(1)修改內容(2)刪除(3)取消,回系統主畫面：'))
    if editoption == 1:
        editcontent = input('修改內容為')
        memo['content'] = editcontent
        print('修改完成！')
    elif editoption == 2:
        memolist.remove(memo)
        print('刪除完成！')
    elif editoption == 3:
        option = eval(input('歡迎來到主要功能列表，請選取一項主要功能：')) 

def export_memolist():
    import csv
    user_export = input('請輸入大名：')
    fn = user_export + '_memo_history.csv'
    with open(fn, 'w', newline = '') as csvFile:
        csvW = csv.writer(csvFile)
        for item in memolist: 
            csvW.writerow(item.values())
    print('輸出完成！')

def import_memolist():
    import csv
    user_import = input('請輸入大名：')
    fn = user_import + '_memo_history.csv'
    with open(fn, 'r') as csvFile:
        csvR = csv.reader(csvFile)
        listcsv = list(csvR)
    if len(memolist) == 0:
        for row in listcsv:
            memodict = {'date': row[0],
                    'content': row[1]}
            memolist.append(memodict)
    else:
        for row in listcsv:
            memodict = {'date': row[0],
                    'content': row[1]}
            for memo in memolist:
                if row[0] == memo['date']:
                    break
                    memolist.append(memodict)


# In[ ]:




