def check_brackets(string):
    stack = []
    result = ''
    
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += '?'
    
    for index in stack:
        result += 'x'
    
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
