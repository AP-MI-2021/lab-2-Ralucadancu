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

test_get_largest_prime_below()
test_is_superprime()
        
          
