'''問題描述【黑洞數】
黑洞数又称陷阱数，是指任何一个数字不全相同的整数，
在经过有限次“重排求差”操作后，总会得到某一个或一些数，这些数即为黑洞数。

“重排求差”操作是将组成一个数的各位数字重排，将得到的最大数减去最小数。
例如，207的“重排求差”操作序列是：720-027=693，963-369=594，954-459=495，
此时再进行“重排求差”操作不会发生改变。再用208计算一次，也是停止到495，所以495是三位黑洞数。
'''
'''算法設計
-將任意一個三位數進行拆分
-拆分後的數據重新組合，將可以組合的最大值減去最小值，差值賦給變量j
-將當前差值暫存到另一變量h中：h= j
-對變量j執行拆分，重組，求差操作，差值仍存儲到變量j
-判斷當前差值j是否於前一次差值h相等，若相等則將差值輸出並結束循環，否則重複步驟3-5
'''

# 求三位數的組合最大值
# a,b,c分別對應百位，十位，個位
def three_max(a,b,c):
    if a<b:
        t = a 
        a = b 
        b = t 
    if a<c:
        t = a
        a = c 
        c= t 
    if b<c:
        t = b 
        b = c
        c = t 
    return a*100 + b*10 +c 

def three_min(a,b,c):
    if a<b:
        t = a 
        a = b 
        b = t 
    if a<c:
        t = a
        a = c 
        c= t 
    if b<c:
        t = b 
        b = c
        c = t 
    return c*100 + b*10 +a 


# 求黑洞數
def black_number(max,min):
    j = max - min 
    # k 控制循環次數
    k = 0 
    while k < min:
        # h記錄上一次最大值與最小值的差
        h = j 
        hun = j//100 
        ten = j%100//10
        bit = j%10 
        max = three_max(hun,ten,bit)
        min = three_min(hun,ten,bit)
        j = max - min 
        if j == h:
            # 最後兩次差相等，差極為所求的黑洞數
            print("%d"%j)
            break 
        k+= 1
    
if __name__ =="__main__":
    i = int(input("請輸入一個三位整數"))
    hun = i//100
    ten = i%100//10
    bit =i%10 
    max = three_max(hun,ten,bit)
    min = three_min(hun,ten,bit)
    print("max = ",max)
    print("min = ",min)
    black_number(max,min)