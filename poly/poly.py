import itertools
s="ADFGX"
sumresult=[]
numsumresult=[]
ciper="AXAXDFDXXAFADFGFXAADFGDXGFDXFFDFAXDXFFFFXGXGAAXAGAFDDXFFDXFFDXDXDXDXGFDFAXFXAADXAAGAXGDGXAXAFAXXFFXADFFGAADXDXAXDFDFDXXAXXDXDAAAAAFAXAAAFGGAFGFGXADXXADFGADXDFDFGAGFDGAXFGAXDGDADXFFFFDAGFADXGDX"
for i in itertools.permutations(s,5):#找出所有全排列
    sumresult.append("".join(i))
for i in sumresult:
    temp=""
    for j in ciper:
        temp+=str(i.index(j)+1)
    numsumresult.append(temp)
for i in numsumresult:
    ans_=""
    for j in range(0, len(i),2):
        xx=(int(i[j])-1)*5+int(i[j+1])+96
        if xx>ord('i'):
            xx+=1
        ans_+=chr(xx)
    print(ans_)



