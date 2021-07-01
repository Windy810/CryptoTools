from pycipher import ADFGX
from random import shuffle 
import random,string

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
str='AXAXDFDXXAFADFGFXAADFGDXGFDXFFDFAXDXFFFFXGXGAAXAGAFDDXFFDXFFDXDXDXDXGFDFAXFXAADXAAGAXGDGXAXAFAXXFFXADFFGAADXDXAXDFDFDXXAXXDXDAAAAAFAXAAAFGGAFGFGXADXXADFGADXDFDFGAGFDGAXFGAXDGDADXFFFFDAGFADXGDX'
while(1):
    zimu='btalpdhozkqfvsngicuxmrewy'
    # zimulist=[]
    # for i in zimu:
    #     zimulist.append(i)
    # shuffle(zimulist)
    # zimu=''
    # for i in zimulist:
    #     zimu+=i
    keyword=random_char(5)
    a=ADFGX(zimu,keyword)
    out = a.decipher(str)
    if "flag" in out:
        print(out,zimu,end="\n")

    
    #AHKKZEIZCVFIXSEFQKVZYQFHQOFAYLFBCZFQPNOLVCVZFEKBOLNHOVIFKUKFSPNNIIPPCILKXFQKSHHKECZBAKZKINNKSKAN