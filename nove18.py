def python():
    for i in 'python':
        print(i)
# python()

def value():
    a=5
    for i in range(1,a+1):
        for j in range(1,i+1):
            print('*',end='')
        print('hi')
# value()

def python1():
    i=0
    a='python'
    for i in range(0,len(a)):
        for j in range(0,i+1):
            print(a[j],end='')
        print()
python1()