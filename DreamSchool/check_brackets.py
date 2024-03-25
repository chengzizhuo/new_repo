def check_brackets(string):
    stack = []  #用栈来进行括号配对
    result = ''
    
    for i, char in enumerate(string):
        if char == '(':   #左括号进栈
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()  #当前为右括号且栈中有未配对的左括号，则配对成功，左括号弹出
            else:
                result += '?' #无可配对左括号，输出？
    
    for index in stack:
        result += 'x'  #剩余未配对左括号，输出x
    
    return string + '\n' + result

# 测试用例
test_cases = [
    "bge)))))))))",
    "((IIII))))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for test_case in test_cases:
    print(check_brackets(test_case))
