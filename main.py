" Prima problema "

def get_largest_prime_below(n):
    if n<=2:
        print("Nu exista")
    else:
        while True:
            n= n-1
            ok=True
            for i in range (2,n):
                if n%i==0:
                    ok=False
                    break
            if ok == True:
                print (n)
                break

def test_get_largest_prime_below():
      n=int(input("1) n= "))
      get_largest_prime_below(n)


"Problema numarul 6"

def is_superprime(n):
    while n!=0:
        if n<2:
            return False
        for i in range (2,n):
            if n%i==0:
                return False
        n= n// 10
    return True

def test_is_superprime():
    n=int(input("6) n="))
    if is_superprime(n):
        print("Este Superprim")
    else:
        print("Nu este superprim ")




"Problema numarul 3"

def is_prime(n):

    if (n==0 or n==1):
      return False
    for d in range (2,n//2):
        if (n%d==0):
          return False
    return True

def get_goldbach(n):
    ok=True
    for i in range (2,n//2+1):
        p1=i
        p2=n-i
        if is_prime(p1) and is_prime(p2):
            ok=False
            print (p1,p2)
            break
        if ok==True:
           print("Nu are proprietatea")
           

def test_get_goldbach():
    n=int(input("3) n="))
    get_goldbach(n)
                       

test_get_largest_prime_below()
test_is_superprime()
test_get_goldbach()


