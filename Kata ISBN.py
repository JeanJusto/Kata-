
import re

def isValidISBN( code ):

    code = code.replace('-', '').replace(' ', '')
    return  {
        10 : isValidISBN10,
        13 : isValidISBN13
    }.get( len(code), lambda n: False)( code )

def isValidISBN10( code ):

    result = False
    
    # isbn10 string have 10 chars.
    # First 9 chars should be numbers and the 10th char can be a number or an 'X'      
    if re.match('^\d{9}[\d,X]{1}$', code):
        sum = 0

        # result = (isbn[0] * 1 + isbn[1] * 2 + ... + isbn[9] * 10) mod 11 == 0
        for i in range(0, 9):
            sum += int(code[i]) * (i + 1)
        
        sum += 10 if code[9] == 'X' else int(code[9]) * 10

        result = sum % 11 == 0

    return result

def isValidISBN13( code ):
    
    result = False

    # isbn13 string have 13 chars. All of them should be numbers. 
    if re.match('^\d{13}$', code):
        sum = 0

        # result = (isbn[0] * 1 + isbn[1] * 3 + ... + isbn[12] * 1) mod 10 == 0
        for i in range(len(code)):
            digit = int(code[i])
            sum += digit * (3 if isOdd(i) else 1)
        
        result = sum % 10 == 0

    return result

def isOdd( n ): 
    return n % 2 != 0

isbns = [
    "0-7167-0344-0",
    "978-0-7167-0344-0",
]

for isbn in isbns:
    print ( "{0} is valid ISBN code? {1}".format(isbn, isValidISBN(isbn)) )
