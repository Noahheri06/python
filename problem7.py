import math

pi = math.pi

def main():
    x = 1
    y = -2
    best = 1
    for i in range(1000000000):
        ans = check_formula(x, y)
        if abs(1 - ans) < best:
            best = abs(1 - ans)
            print(f"x is {x}, y is {y}, ans is {ans}")
        if ans < 1:
            x += 1
        else:
            y -= 1
    

def check_formula(x, y):
    return (5 * x + pi * y)

main()
