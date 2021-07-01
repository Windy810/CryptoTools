import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator
import binascii

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    # test_hack_RSA()
    e = 932333292871340311536583425772799788581476608800501618257200913635688712797956595013312457091949241781390707236218326324287260096872275100972804737277188856396706341586791458364387568557914836880210799183882901779150174060503451992261799576875742788774243390310560719634789720219992974946820314802939572580353
    n = 1083178419603719448638799632475202672644727971741749926078568673467491721729891939162664192885208434541370193744078154888072589708037117486860213089624795029582525501783298026959443870222339003799747202112246474259375161019073230508249672271697738321500894559008261698558072028050806042318719109646040290668273
    c = 629671321698958970045785762020010033814849277886377341930329645318473402676175912514800812974363555981287129835454344489639514895119374277833430799149513068930055615330516662428479865724507981237582779353644800423513485357718723908554543915240117995464419165823214748496569735844685568687856495834900999682293
    d=hack_RSA(e, n)
    print('d=',d)
    m=pow(c, d,n)
    print('m=',m)
    b = hex(m)  #转换成相同的字符串即'0x665554'
    b = b[2:]   #截取掉'0x'
    c = binascii.a2b_hex(b) #转换成ASCii编码的字符串
    print(c)
