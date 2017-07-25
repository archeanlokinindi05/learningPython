from sys import *
import re
with open("myfile.py","r") as file:
    data=file.readlines()
    str=data
scanner=re.Scanner([(r"[0-9]+", lambda scanner,token:("INTEGER", token)),
                    (r"[=+*-/]", lambda scanner,token:("MATHEMATICAL SYMBOL",token)),
		    (r"[a-z_]+", lambda scanner,token:("IDENTIFIER", token)),
		    (r"[,.!@]+", lambda scanner,token:("PUNCTUATION", token)),
                    (r"[(]+", lambda scanner,token:("LEFT ANGULAR BRACES", token)),
                    (r"[)]+", lambda scanner,token:("RIGHT ANGULAR BRACES", token)),
                    (r"[{]+", lambda scanner,token:("LEFT CURLY BRACES", token)),
                    (r"[}]+", lambda scanner,token:("RIGHT CURLY BRACES", token)),
                    (r"[[]+", lambda scanner,token:("LEFT SQUARE BRACES", token)),
                    (r"[]]+",lambda scanner,token:("RIGHT SQUARE BRACKET",token)),
		    (r"\s+",None),
		    ])
result=scanner.scan(str)
print(result)
    

