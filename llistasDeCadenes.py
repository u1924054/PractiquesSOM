
#No funciona be ja que durant la comparació tambe mira els espais en blanc pero he practicat les funcions 

string = input('Introdueix una frase:\n')
reverseString = string [:: -1]

def esPalindrom(s1, s2):
    if string.strip() == reverseString.strip():
        return True
    else:
        return False

if esPalindrom(string, reverseString):
    print('Es palindrom')
else: 
    print('No es palindrom')