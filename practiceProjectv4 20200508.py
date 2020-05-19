#!/usr/bin/env python
# coding: utf-8

# In[1]:


#這次主題：做一個備忘錄
#功能包含歡迎畫面,新增,顯示全部,查詢內容（修改,刪除,返回上層),輸出/匯入檔案（可以設定輸出/匯入到自己專有名字的檔案）,退出系統

#功能1: 新增備忘錄（填入日期和內容）,可以在主要功能列表跳出畫面重複新增
#功能2: 顯示全部備忘錄（只有顯示日期）, 會顯示目前所有的備忘錄
#功能3: 查詢備忘錄（輸入日期後可以顯示內容）, 如果輸錯日期會跳錯誤訊息
#可以再選擇修改（對內容作修改）/刪除（對目前這個備忘錄刪除）/取消 (跳出主要功能列表)
#功能4: 可以輸出目前的備忘錄到csv檔案, 可以指定檔案名稱是自己的名字
#功能5: 可以匯入指定檔案名稱是自己的名字的csv檔案（匯入後可以用功能2看目前匯入的所有備忘錄）

#demo: 顯示全部備忘錄(還沒有任何備忘錄) -> 新增備忘錄（填入日期和內容）-> 查詢備忘錄（輸入日期後可以顯示內容和錯誤訊息）
#-> 可以修改或刪除或跳出 -> 輸出目前紀錄 -> 匯入您歷史備忘錄 -> 輸出目前紀錄 (只會出現剛剛已經紀錄在歷史備忘錄裡面的東西)
#-> 退出系統


# In[2]:


import practiceProjectv4_functions

practiceProjectv4_functions.welcomepage()

while True:
    option = eval(input('歡迎來到主要功能列表，請選取一項主要功能：'))
    if option == 1:
        practiceProjectv4_functions.add_memo_dict()
        print('')
    elif option == 2:
        practiceProjectv4_functions.show_memo_dict()
        print('')
    elif option == 3:
        practiceProjectv4_functions.search_memo_dict()
        print('')
    elif option == 4:
        practiceProjectv4_functions.export_memolist()
        print('')
    elif option == 5:
        practiceProjectv4_functions.import_memolist()
        print('')
    else:
        print('成功退出系統 ✿。・ﾟﾟ･✿。・ﾟﾟ･✿。・ﾟﾟ･✿ლ (́◕◞౪◟◕‵)')
        break


# In[ ]:





# In[ ]:




