'''

We want to build a simple calculator that can solve arithmetic expressions like 2 + 2 or 4 * 5 - 10 * 2. Write a function calc(expr) that accepts a string as input and returns the answer as a number. It should follow the normal order of operations and support addition, subtraction, multiplication, and division. Don't worry about parentheses or improperly formatted strings.

Examples

calc("1 + 1")       # => 2
calc("5 - 1 - 1")   # => 3
calc("84 / 1 / 2")  # => 42
calc("5/2 - 2*3")   # => -3.5


'''

def calc(expr):
  print(expr)
  for op in ['+', '-', '*', '/']:
    if op in expr:
      left, right = expr.rsplit(op, 1)
      print(left, right)
      if op == '+': return calc(left) + calc(right)
      if op == '-': return calc(left) - calc(right)
      if op == '*': return calc(left) * calc(right)
      if op == '/': return calc(left) / calc(right)

  # Base case: no more operators
  return float(expr.strip())

#print(calc("1+1"))
#print(calc("5 - 1 - 1") )  # => 3
#print(calc("84 / 1 / 2"))  # => 42
print(calc("5/2 - 2*3"))   # => -3.5