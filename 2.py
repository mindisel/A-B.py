def add(x,y):
    return x+y
C=input('A B 숫자를 입력하시오 :')
while True:
    A=int(C.split(' ')[0]) # C.split(' ')[0] = int(A)
    B=int(C.split(' ')[1]) # C.split(' ')[1] = int(B)
    if 0<A<10 and 0<B<10:
        print(add(A,B)) 
        C=input('A B 숫자를 입력하시오')
    else:
        print('다시 입력하시오') 
        C=input('A B 숫자를 입력하시오 :')
     
