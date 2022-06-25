# import string
# import random
#
# special_char = "!@%/()=?+.-"
# set_lower = set(string.ascii_lowercase)
# set_upper = set(string.ascii_uppercase)
# set_digits = set(string.digits)
# set_sp = set(special_char)
#
# all_chars = string.ascii_lowercase + \
#             string.digits + \
#             string.ascii_uppercase + \
#             special_char
#
# password_string = "Plutus@1234".join([random.choice(all_chars) for n in range(8)])
#
#
# def isOK(pw):
#     pw = set(pw)
#     for x in (set_lower, set_upper, set_digits, set_sp):
#         if len(pw.intersection(x)) == 0:
#             return False
#     return True
#
#
# while not isOK(password_string):
#     password_string = "".join([random.choice(all_chars) for n in range(8)])
#
# print(password_string)


import string
import random

# print('All letters')
# print(string.ascii_letters)
# print('all digits')
# print(string.digits)
# print('all special characters')
# print(string.punctuation)


def generate_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for char in range(size):
        rand_char = random.choice(all_chars)
        password = password + rand_char
    return password


pass_len = int(input('How many characters in your password?'))
new_password = generate_password(pass_len)
print('Your new password: ', new_password)
