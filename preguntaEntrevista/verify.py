# create two lists, one with ( { [ and the other with ) ] }
from typing import final

openings = ['(', '{', '[']
closings = [')', '}', ']']

stringTrue = "(()[]{})"
stringFalse = "((})[]{})"

finalString = stringFalse


#             ^   ^
# stringTrue = "( [ ] { } )"
#              ^         ^

# al encontrar un (, encuentra el siguiente ) y lo saca de finalString

def checkBase(s):
    # check if there is an even amount of () [] {}
    if s.count('(') == s.count(')'):
        if s.count('[') == s.count(']'):
            if s.count('{') == s.count('}'):
                return True
    return False


def checkNext(s,finalString = finalString):
    print(finalString)

    for i in s:
        if i in openings:
            for x in s:
                if x in closings:
                    # remove i and x from finalString
                    finalString = finalString.replace(i, "")
                    finalString = finalString.replace(x, "")
                    print("removing")
                else:
                    print("not removing")
    
    if len(finalString) == 0:
        print("string is valid")
    else:
        print("string is not valid")


def basicTest():
    if checkBase(stringFalse):
        print("True")
    else:
        print("False")
        return

    checkNext(stringFalse)

basicTest()
