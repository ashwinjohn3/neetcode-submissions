def do_operation(a, b, operation):
    if operation == '+':
        return a + b 
    elif operation == '-':
        return a - b 
    elif operation == '*':
        return a * b 
    elif operation == '/':
        return a / b 
    else:
        raise ValueError(f"Unknown operation: {operation}")

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operations = set(["+", "-", "*", "/"])
        numbers = []
        a = None
        b = None
        for token in tokens:
            if token not in valid_operations:
                numbers.append(token)
            elif token in valid_operations:
                b = int(numbers.pop())
                a = int(numbers.pop())
                numbers.append(do_operation(a, b , token))
        return int(numbers[0])
                
        

        