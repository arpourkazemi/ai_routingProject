def print_yellow(text):
    print("\033[33m" + text + "\033[m")


def print_green(text):
    print("\033[32m" + text + "\033[m")


def print_red(text):
    print("\033[31m" + text + "\033[m")


def print_blue(text):
    print("\033[36m" + text + "\033[m")


def print_purple(text):
    print("\033[35m" + text + "\033[m", end="")


def print_danger(text):
    print("\033[37;41m" + text + "\033[m")
    print()
