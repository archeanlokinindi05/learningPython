import re
from sys import *

scanner=re.Scanner([(r"[0-9]+", lambda scanner,token:("INTEGER", token)),   # Scanner scans for Integers and returns it
                    (r"[=+*-/%#^]", lambda scanner,token:("SPECIAL SYMBOL",token)),  #Scanner scans for symbols like =+*-/ and returns it
		    (r"[a-zA-Z_@0-9a-zA-Z]+", lambda scanner,token:("IDENTIFIER", token)),  #Scanner scans for Identifiers a-z_@ and returns it
		    (r"[,.!?]+", lambda scanner,token:("PUNCTUATION", token)), #Scanner scans for Punctuations and returns it
                    (r"[(]+", lambda scanner,token:("LEFT PARANTHESES", token)), #Scanner scans for ( braces and returns it
                    (r"[)]+", lambda scanner,token:("RIGHT PARANTHESES", token)),#Scanner scans for ) braces and returns it
                    (r"[{]+", lambda scanner,token:("LEFT CURLY BRACES", token)), #Scanner scans for { braces and returns it
                    (r"[}]+", lambda scanner,token:("RIGHT CURLY BRACES", token)), #Scanner scans for } braces and returns it
                    (r"[[]+", lambda scanner,token:("LEFT BRACKET", token)), #Scanner scans for [ braces and returns it
                    (r"[]]+",lambda scanner,token:("RIGHT BRACKET",token)), #Scanner scans for ] braces and returns it
                    (r"[<>|&]+",lambda scanner,token:("UNIQUE SYMBOLS",token)), #Scanner scans for <>|& and returns it
                    (r"[']+",lambda scanner,token:("CHARACTER LITERALS",token)), #Scanner scans for ' and returns it
		    (r"\s+",None), #Scanner matches any whitespace character
		    ])

str=input('Enter String to be tokenized:')  #Enter string to be tokenized
result,remainder=scanner.scan(str) 
print(result)

