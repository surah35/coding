from cmath import sqrt


phrase = "HELLEO WORLD"
#將字串變成小寫子母
print(phrase.lower())
#將字串變成大寫字母
print(phrase.upper())
#判斷字母是否全為大寫，
#若是大寫會return ture
#若不是大寫會return false
print(phrase.isupper())
#判斷字母是否全為小寫
print(phrase.islower())
#將H替換成h
print(phrase.replace("H","h"))
#------------------------------------------------
number = 18
#對數字取絕對值
print(abs(number))
#對數字開根號
print(sqrt(number))

#列表(list):內容可被修改
h = [20,50,70,90,20,30,20]
#元組(tuple):內容不可被修改
g=(20,60,50,40,30,60)

print(h.index(20))
print(h[0])
#清空列表
h.clear()
print(h)
#計算列表中有幾個90
print(h.count(90))

f = str(200)
sum = int(f[0])+int(f[1])+int(f[2])
print(sum)

file = open("123.txt",mode = "r")
#h = len(file.readlines())
print(file.readlines())
file.close()