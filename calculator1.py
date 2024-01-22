# Demonstrates defining a function with a return value

def square(n:float) -> float:
    return n * n


def main():
    x = float(input("What's x? "))
    print("x squared is", square(x))


if __name__ == "__main__":
    main()
