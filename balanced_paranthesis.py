def balanced(exp):
    stack=[]
    for char in exp:
        if char in ["[","{","("]:
            stack.append(exp)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True

exp="[{){}{)(){{})({[]})]"
if balanced(exp):
    print("balanced")
else:
    print("not balanced")
