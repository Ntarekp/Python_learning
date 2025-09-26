def combined(a, b, /, c, *, d, e):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")
    return a + b + c + d + e

# Usage examples:
combined_example(1, 2, 3, d=4, e=5)        # c is positional, d and e are keyword-only
combined_example(1, 2, c=3, d=4, e=5)      # c can also be passed as keyword

def addition(a,b,/,c, d):
    return a + b + c +d 

addition(1, 2, 3, 4)
addition(1, 2, c=3, d=4)
addition(1, 2, 3, d=4)
addition(1, 2, c=3, d=4)

# Position only arguments
def multiplication (a, b,*,c,d):
    return a*b*c*d


print(multiplication(1,2,3, c=3, d=4))