from sympy import symbols, simplify
x = symbols('x')
simplify( (x - 1/x)*(1/x - 1/(x-1)) + 1/x )
simplify( (1 - ((1/x + 1)/(1/x) - 1)/(1/x))/((x+1)/x))