# create two lists, one with ( { [ and the other with ) ] }
openings = ['{', '[', '(']
closings = ['}', ']', ')']

cache = []

def verify(string):
    for char in string:
        # print(char)
        if char in openings:
            cache.append(char)
            # print("apending " + char)
        elif char in closings:
            if check(char):
                cache.pop()
                # print("popping " + char)
            else:
                # print("False " + char)
                return print("string doesnt work")


    if len(cache) == 0:
        print('OK')
        


def check(char):
    #if char is '}' and cache[-1] is '{':
    #    return True
    #elif char is ']' and cache[-1] is '[':
    #    return True
    #elif char is ')' and cache[-1] is '(':
    #    return True
    #else:
    #    return False
    # hard code the if statements using == instead of is
    if char == '}' and cache[-1] == '{':
        return True
    elif char == ']' and cache[-1] == '[':
        return True
    elif char == ')' and cache[-1] == '(':
        return True
    else:
        return False

verify("({[})")
