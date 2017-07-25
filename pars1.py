import re
import string
import sys

scanner=re.Scanner([(r"[0-9]+", lambda scanner,token:("INTEGER", token)),  
                    (r"[=+*-/]", lambda scanner,token:("OPERATORS",token)), 
                    (r"^[int|char|bool|if|while|return|read|write|string]+",lambda scanner,token:("Keywords",token)), 
		    (r"[a-zA-Z_@0-9a-zA-Z]+", lambda scanner,token:("IDENTIFIER", token)),  
                    (r"^[int|char|bool|if|while|return|read|write|string]+",lambda scanner,token:("Keywords",token)),
                    (r"^[a-zA-z()]*",lambda scanner,token:("Function Identifier",token)),
                    (r"[(]+", lambda scanner,token:("Left Parantheses", token)), 
                    (r"[)]+", lambda scanner,token:("Right Parantheses", token)),
                    (r"[{]+", lambda scanner,token:("Left Curly Braces", token)), 
                    (r"[}]+", lambda scanner,token:("Right Curly Braces", token)),
                    (r"[[]+", lambda scanner,token:("Left Bracket", token)), 
                    (r"[]]+",lambda scanner,token:("Right Bracket",token)), 
                    (r"[<]+",lambda scanner,token:("Left Angular Braces",token)), 
                    (r"[>]+",lambda scanner,token:("Right Angular Braces",token)), 
                    (r"[;:]+",lambda scanner,token:("Special Symbol",token)),
		    (r"\s+",None),
		    ])

x=input('Enter Input File \n 1- Simple_prog \n 2- simple_recur.txt \n' )
print('You have entered:', x)
         
if x== '1':
    str=input('Enter String:')  
    result,remainder=scanner.scan(str) 
    print(result)
    if result[0][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[1][0]== 'Left Parantheses':
        pass
    else:
        print('False')
    if result[2][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[3][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[4][0]=='Right Angular Braces':
        pass
    else:
        print('False')
    if result[5][0]=='Left Angular Braces':
        pass
    else:
        print('False')
    if result[6][0]=='Right Angular Braces':
        pass
    else:
        print('False')
    if result[7][0]=='Left Curly Braces':
        pass
    else:
        print('False')
    if result[8][0]=='IDENTIFIER' or result[8][0]=='Keywords':
        pass
    else:
        print('False')
    if result[9][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[10][0]=='INTEGER':
        pass
    else:
        print('False')
    if result[11][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[12][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[13][0]=='Right Curly Braces':
        print('True')
    else:
        print('False')
        

if x== '2':
    str=input('Enter String:')  
    result,remainder=scanner.scan(str) 
    print(result)
    if result[0][0]=='IDENTIFIER' or result[0][0]=='Keywords':
        pass
    else:
        print('False')
    if result[1][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[2][0]=='Keywords' or result[2][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[3][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[4][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[5][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[6][0]=='Right Angular Braces':
        pass
    else:
        print('False')
    if result[7][0]=='Left Angular Braces':
        pass
    else:
        print('False')
    if result[8][0]=='Keywords' or result[8][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[9][0]=='Right Angular Braces':
        pass
    else:
        print('False')
    if result[10][0]=='Left Curly Braces':
        pass
    else:
        print('False')
    if result[11][0]=='Keywords' or result[11][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[12][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[13][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[14][0]=='Keywords' or result[14][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[15][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[16][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[17][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[18][0]=='INTEGER':
        pass
    else:
        print('False')
    if result[19][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[20][0]=='Left Curly Braces':
        pass
    else:
        print('False')
    if result[21][0]=='Keywords' or result[21][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[22][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[23][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[24][0]=='Right Curly Braces':
        pass
    else:
        print('False')
    if result[25][0]=='Keywords' or result[24][0]=='IDENTIFIER':
        pass
    else:
        pass
    if result[26][0]=='Left Curly Braces':
        pass
    else:
        print('False')
    if result[27][0]=='Keywords' or result[25][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[28][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[29][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[30][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[31][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[32][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[33][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[34][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[35][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[36][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[37][0]=='INTEGER':
        pass
    else:
        print('False')
    if result[38][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[39][0]=='Keywords' or result[39][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[40][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[41][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[42][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[43][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[44][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[45][0]=='Right Curly Braces':
        pass
    else:
        print('False')
    if result[46][0]=='Right Curly Braces':
        pass
    else:
        print('False')
    if result[47][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[48][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[49][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[50][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[51][0]=='Right Angular Braces':
        pass
    else:
        print('False')
    if result[52][0]=='Left Angular Braces':
        pass
    else:
        print('False')
    if result[53][0]=='Right Angular Braces':
        pass
    else:
        print('False')
    if result[54][0]=='Left Curly Braces':
        pass
    else:
        print('False')
    if result[55][0]=='IDENTIFIER' or result[55][0]=='Keywords':
        pass
    else:
        print('False')
    if result[56][0]=='IDENTIFIER': 
        pass
    else:
        print('False')
    if result[57][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[58][0]=='IDENTIFIER': 
        pass
    else:
        print('False')
    if result[59][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[60][0]=='OPERATORS':
        pass
    else:
        print('False')
    if result[61][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[62][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[63][0]=='INTEGER':
        pass
    else:
        print('False')
    if result[64][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[65][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[66][0]=='IDENTIFIER' or result[66][0]=='Keywords':
        pass
    else:
        print('False')
    if result[67][0]=='Left Parantheses':
        pass
    else:
        print('False')
    if result[68][0]=='IDENTIFIER':
        pass
    else:
        print('False')
    if result[69][0]=='Right Parantheses':
        pass
    else:
        print('False')
    if result[70][0]=='Special Symbol':
        pass
    else:
        print('False')
    if result[71][0]=='Right Curly Braces':
        print('True')
    else:
        print('False')
    


    
    
