def countwords():
    word=" java is a programming language"
    reset=True
    count=0
    i=0
    while i<len(word):
        if reset==True and word[i]!=' ':
            count+=1
            reset=False
        elif word[i]==' ':
            reset=True
        i+=1
    return count
# print(countwords())
def checkdigitsonly():
    word='12345'
    for i in word:
        if not('0'<=i<='9'):
            return False
    return True

# print(checkdigitsonly())

def countuplc():
    word='jayaPriAN'
    upper=0
    lower=0
    for i in word:
        if 'a'<=i<='z':
            lower+=1
        elif 'A'<=i<='Z':
            upper+=1
    return [lower,upper]
print(countuplc())

def removeallvowels():
    a='jayapriyan'
    j=''
    for i in a:
        if i not in ('aeiou'):
            j+=i
    return j
print(removeallvowels())

def firstrepeate():
    data='jayapriyan'
    dict1={}
    for i in data:
        if i not in dict1:
            dict1[i]=1
        else:
            return i
    return None
print(firstrepeate())

        