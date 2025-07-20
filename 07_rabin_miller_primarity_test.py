import random

def is_probably_prime(number, rounds=5):

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    b = 0
    m = number - 1
    while m % 2 == 0:
        m //= 2
        b += 1

    for _ in range(rounds):
        a = random.randrange(2, number - 1)
        z = pow(a, m, number)
        if z == 1 or z == number - 1:
            continue  # Go to next round

        for iteration in range(b - 1):
            z = pow(z, 2, number)
            if z == number - 1:
                break
        else:
            return False

    return True  


p = 137
if is_probably_prime(p):
    print(f"{p} is probably prime.")
else:
    print(f"{p} is composite.")
