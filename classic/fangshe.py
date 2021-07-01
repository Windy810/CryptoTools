#仿射密码解密
#改进欧几里得算法求线性方程的x与y
def get(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a //b
        remainder = a % b
        x1, y1 = get(b, remainder)
        x, y =y1, x1 - k * y1
    return x, y
 
s = input("请输入解密字符：").upper()
a = int(input("请输入a："))
b = int(input("请输入b："))
 
#求a关于26的乘法逆元
x, y = get(a, 26)
a1 = x % 26
 
l= len(s)
for i in range(l):
    cipher = a1 * (ord(s[i])- 65 - b) % 26
    res=chr(cipher + 65)
    print(res, end='')