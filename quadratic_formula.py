import math

def calc(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"{root1:.3f}",  f"{root2:.3f}"
        
user_input = input()
values = user_input.split()
data = [int(value) for value in values]
result = calc(data[0], data[1], data[2])

print(result)
