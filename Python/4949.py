while True:
    stack = []
    w = input()

    if w == '.':
        break

    for i in w:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('no')
    else:
        print('yes')