'''
5 * 4 - 3 - 5 ^ 3

5 * 4 ^ 2

Given an expr with - * and ^ , eval it ?

eliminate all ^
eliminate all *
eliminate all -

'''


def eval_exp(expr):
    expr = expr.replace(" ", "") #O(N) replace empty space
    expr_list = [ch for ch in expr]
    expr = expr_list
    print(expr)

    

expr = "4^3^2-9"
print(eval_exp(expr))