def main():
    phone_number= input('Please enter a phone number in the format XXX-XXX-XXXX: ')
    validNumber(phone_number)
    translateNumber(phone_number)

def validNumber(phone_number):
    for i,c in enumerate(phone_number):
        if i in [3,3,4]:
            if c != '':
                phone_number=input('Please enter a valid phone number: ')
        return phone_number
        elif not c.isalnum():
        phone_number=input('Please enter a valid phone number: ')
        return phone_number
        return phone_number


def translateNumber(phone_number):
    s = ""
    for char in phone_number:
        if char is '1':
            x1 = '1'
            s = s + x1
        elif char is '-':
            x2 = '-'
            s = s + x2
        elif char in 'ABCabc':
            x3 = '2'
            s = s + x3
        elif char in 'DEFdef':
            x4 = '3'
            s = s + x4
        elif char in 'GHIghi':
            x5 = '4'
            s = s + x5
        elif char in 'JKLjkl':
            x6 = '5'
            s = s + x6
        elif char in 'MNOmno':
            x7 = '6'
            s = s + x7
        elif char in 'PQRSpqrs':
            x8 = '7'
            s = s + x8
        elif char in 'TUVtuv':
            x9 = '8'
            s = s + x9
        elif char in 'WXYZwxyz':
            x10 = '9'
            s = s + x10

            print(s)
