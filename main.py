# import math

# def score(x, y):
#     if (x >= -1 and x <= 1) and y >= -1 and y <= 1:
#         return 10
#     if (x > 1 and x <= 5) or (x < -1 and x >= -5) and (y > 1 and y <= 5) or (y < -1 and y >= -5):
#         return 5
#     if (x > 5 and x <= 10) or (x < -5 and x >= -10) and (y > 5 and y <= 10) or (y < -5 and y >= -10):
#         return 1
#     return 0

def scorecalc(x, y):
    # inner circle
    if (x**2 + y**2 < 1**2) or (x**2 + y**2 == 1**2):
        return 10
    # middle circle
    if (x**2 + y**2 > 1**2) and ((x**2 + y**2 < 5**2) or (x**2 + y**2 == 5**2)):
        return 5
    # outer circle
    if (x**2 + y**2 > 5**2) and ((x**2 + y**2 < 10**2) or (x**2 + y**2 == 10**2)):
        return 1
    return 0



while True:
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    try:
        float(x)
        float(y)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


result = scorecalc(x, y)
print(f"You scored {result} points!")
