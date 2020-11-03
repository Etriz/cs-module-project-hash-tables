# Your code here
import math, random

new_dict = dict()


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= x + y
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    hash_key = hash(f"{x, y}") % 50000
    if new_dict.get(hash_key) is not None:
        return new_dict[hash_key]

    v = math.pow(x, y)
    v = math.factorial(v)
    v //= x + y
    v %= 982451653

    new_dict[hash_key] = v

    return new_dict[hash_key]


# (slowfun(11, 3))  # 246727355
# print(new_dict)

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f"{i}: {x},{y}: {slowfun(x, y)}")
