import random
import array
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blu


print(B+""" 
 ___  ____ ____ ____ _ _ _ ____ ____ ___  
 |__] |__| [__  [__  | | | |  | |__/ |  \ 
 |    |  | ___] ___] |_|_| |__| |  \ |__/ 
                                          

 ____ ____ _  _ ____ ____ ____ ___ ____ ____ 
 | __ |___ |\ | |___ |__/ |__|  |  |  | |__/ 
 |__] |___ | \| |___ |  \ |  |  |  |__| |  \ 
                                             """)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")                                                                                          
                                             
print(""+O+ """
[+]Tool name: Password-Generator
[+]Creator:AnonGreyHat(Pro Cracker)
[+]Team: Dark Exploit Hacker
[+]Github: https://github.com/anongreyhat
[+]Contact me on whatsapp:+2349042794223
""")
print(""+G+"Hello, Welcome To Password Generator!\n")
MAX_LEN = 12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<' ]

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 

password = ""
for x in temp_pass_list:
        password = password + x
print("password: " +N+ password)
