# It seems as if Code Climate counts SLOC. For this file it reports 8 lines of
# code.
#
# This code violates the first maintainability check `argument-count`


def print_it(a, b, c, d):
    print(a, b, c, d)


def main():
    msg = "Hej Code Climate, please check this code."
    a, b, c, d, e, f, g = msg.split()
    print_it(a, b, c, d)


if __name__ == '__main__':
    main()
