def addCommas(number):
    # reverse a string in python: s[::-1]
    return "".join([(","+s) if (i%3==0 and i!=0) else s for i,s in enumerate(str(number)[::-1])])[::-1]

if __name__ == '__main__':
    print addCommas(1)
    print addCommas(10)
    print addCommas(1000)
    print addCommas(11234)
    print addCommas(999999999)