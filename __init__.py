import random



def aluffi_pentinni(x, y):
    result = 0.25 * x**4 - 0.5 * x**2 + 0.1 * x + 0.5 * y**2
    return result


def three_hump_camel_back(x, y):
    result = 2 * x**2 - 1.05 * x**4 + (x**6) / 6 + x * y + y**2
    return result


def main():
    DOMAIN = [1, 2]

    pass


if __name__ == "__main__":
    main()
