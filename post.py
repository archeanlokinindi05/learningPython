import re
import string

list1=[]

def func_list(str):
  for token in expr:
    if token =='<':
      list1.append(token)
      token=token+1
      continue
    if token == 'func':
      print('Func Encountered')
      list1.append(token)
      token=token-1
      func(expr)
      print('True')
      break
    
def func(str):
  for token in result:
    if token == '<':
      list1.append(token)
      token=token+1
      print('True')
      continue
    if token == '<':
      list1.append(token)
      token=token+1
      continue
    if token == '/w+':
      list1.append(token)
      token=token+1
      continue
    if token =='>':
      list1.append(token)
      token=token+1
      continue
    if token == '>':
      list1.append(token)
      token=token+1
      continue
    if token == '(':
      list1.append(token)
      token=token+1
      continue
    if token == '<':
      list1.append(token)
      token=token+1
      continue
    if token == 'vars':
      list1.append(token)
      token=token+1
      continue
    if token =='>':
      list1.append(token)
      token=token+1
      continue
    if token ==')':
      list1.append(token)
      token=token+1
      continue
    if token =='-':
      list1.append(token)
      token=token+1
      continue
    if token == '>':
      list1.append(token)
      token=token+1
      continue
    if token =='<':
      list1.append(token)
      token=token+1
      continue
    if token =='(':
      list1.append(token)
      token=token+1
      continue
    if token =='return_list':
      list1.append(token)
      token=token+1
      continue
    if token ==')':
      list1.append(token)
      token=token+1
      continue
    if token =='>':
      list1.append(token)
      token=token+1
      print('True')
      break
  else:
    print('Not a function')


def var_dec(result):
  list1=[]
  for token in result:
    if token == 'Type' or token == 'int' or token == 'char' or token == 'bool':
      list1.append(token)
      token=token+1
      print('Test')
      print(list1)
      continue
    if token == ' IDENTIFIER' or token == 'vars':
      list1.append(token)
      print('True')
      break
    break
  print('True')


scanner=re.Scanner([(r"[0-9]+", lambda scanner,token:("INTEGER", token)),  
                    (r"[+*-/]", lambda scanner,token:("OPERATORS",token)), 
                     (r"^[int|char|bool]+",lambda scanner,token:("Type",token)), 
		    (r"[a-zA-Z_@0-9a-zA-Z]+", lambda scanner,token:("IDENTIFIER", token)),  
                    (r"[a-z]", lambda scanner,token:("vars", token)),
                    (r"^[a-zA-z()]*",lambda scanner,token:("Function Identifier",token)),
                    (r"[(]+", lambda scanner,token:("Left Parantheses", token)), 
                    (r"[)]+", lambda scanner,token:("Right Parantheses", token)),
                    (r"[{]+", lambda scanner,token:("Left Curly Braces", token)), 
                    (r"[}]+", lambda scanner,token:("Right Curly Braces", token)),
                    (r"[[]+", lambda scanner,token:("Left Bracket", token)), 
                    (r"[]]+",lambda scanner,token:("Right Bracket",token)), 
                    (r"[<]+",lambda scanner,token:("Left Angular Braces",token)), 
                    (r"[>]+",lambda scanner,token:("Right Angular Braces",token)), 
                    (r"^[->]+",lambda scanner,token:("Arrow Symbol",token)),
		    (r"\s+",None),
		    ])

str=input('Enter String:')  
result,remainder=scanner.scan(str) 
print(result)
var_dec(result)
  

def calList(result):
  for token in result:
    if token == '(':
      token=token+1
      list1.append(token)
      continue
    if token == 'arg_list':
      token=token-1
      arg_list(result)
      break
    break

def arg_list(result):
  for token in result:
    if token == '(':
      list1.append(token)
      token=token+1
      continue
    if token == 'arg':
      list1.append(token)
      token=token+1
      continue
    if token == ')':
      list1.append(token)
      token=token+1
      continue
    if token == 'arg_tail':
      arg_tail(result)
      break
    break

def arg_tail(result):
  for token in result:
    if token == ',':
      list1.append(token)
      token=token+1
      print('True')


