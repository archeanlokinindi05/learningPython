import token
import re


class literal_token:
    def __init__(self, value):
        self.value = int(value)
    def nud(self):
        return self.value

class operator_add_token:
    lbp = 10
    def led(self, left):
        right = expression(10)
        return left + right

class end_token:
    lbp = 0


token_pat = re.compile("\s*(?:(\d+)|(.))")

def tokenize(program):
    for number, operator in token_pat.findall(program):
        if number:
            yield literal_token(number)
        elif operator == "+":
            yield operator_add_token()
        else:
            raise SyntaxError("unknown operator")
    yield end_token()

def parse(program):
    global token, next
    next = tokenize(program).next
    token = next()
    return expression()


