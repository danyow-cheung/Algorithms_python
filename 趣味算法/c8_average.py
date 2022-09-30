'''问题描述【平分7筐鱼】

甲、乙、丙三位渔夫出海打鱼，
他们随船带了21只箩筐。当晚 返航时，
他们发现有7筐装满了鱼，还有7筐装了半筐鱼，
另外7筐是 空的，由于他们没有秤，
只好通过目测认为7个满筐鱼的重量是相等 的，7个半筐鱼的重量是相等的。
在不将鱼倒出来的前提下，怎样将 鱼和筐平分为三份?

'''
if __name__ =="__main__":
    print("分鱼方案如下")
    count =0 
    a =[[0]*3 for i in range(3)]
    # 試探第一個人滿筐a[0][0]的值，滿筐數不能>3 
    for i in range(4):
        a[0][0] = i 
        j = i 
        # 試探第二個人滿筐a[1][0]的值，滿筐不能>3
        while j<= 7-i and j<=3 :
            a[1][0] = j 
            a[2][0] = 7- j - a[0][0]
            j+=1 
            if a[2][0]>3:
                # 第三個人滿筐數不能>3
                continue
            if a[2][0] <a[1][0]:
                break# 要求後一人分得滿筐數大於等於前一個人,已排除重複情況
            for k in range(1,6,2):
                a[0][1] = k 
                for m in range(1,7-k,2):# 試探半筐a[1][1]的值，半筐數為奇數s
                    a[1][1] = m 
                    a[2][1] = 7-k-m 
                    # 判斷每個人分到的魚是否為3.5筐，flag為滿足題意的標記變量
                    flag,n = True,0 
                    while flag and n<3:
                        if a[n][0] + a[n][1] < 7  and a[n][0]*2 +a[n][1]==7:
                            #計算應得到的空筐數量
                            a[n][2] = 7-a[n][0]-a[n][1]
                        else:
                            # 不符合題意標記為0
                            flag = False 
                        n+= 1 
                    if flag:
                        count += 1
                        print(f"No.{count},Full basket Semi-basket Empty")
                        for n in range(3):
                            print("fisher",chr(65+n),":",a[n][0],a[n][1],a[n][2])