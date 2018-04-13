def eval_math_expr(expr):
    negate = False
    while True:
        try: 
            if expr[0] == '-': #for negative numbers
                negate = True #because here the numbers are string format
                expr = expr[1:]
            number1 = Test4Num(expr)[0]
            if negate == True:
                number1 = -number1
                negate = False
            end_number1 = Test4Num(expr)[1]
            expr = expr[end_number1:]
            if expr == '':
                return number1
            op = expr[0]
            expr = expr[1:]
            number2 = Test4Num(expr)[0]
            end_number2 = Test4Num(expr)[1]
            result = operation(op, number1, number2)
            number1 = result
            expr = str(number1) + expr[end_number2:]
        except Exception as e:
            print(e)
            break
    return number1


if __name__ == '__main__':
    interactive = False
    if interactive:
        expr = input('Enter your expression:')
        print(expr + '=')
        print(eval_math_expr(expr))
    else:
        for expr, res in {"2": 2, "2*4": 8, "4+8": 12, "100/3": 33, "2^3": 8}.items():
            result = eval_math_expr(expr)
            if res != result:
                print("Computing", expr, "got", result, "instead of", res)