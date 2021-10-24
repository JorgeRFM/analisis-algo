# REcompilado de: 
#https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals

conv = [(1000,'M'), (500,'D'), (100,'C'), (50,'L'), (10,'X'), (5,'V'), (1,'I')]

def roman(num):

    rom = ''

    while(num > 0):
        for n,r in conv:
            while num >= n:
                rom = rom + r
                num = num - n
    return rom

print(roman(52))
