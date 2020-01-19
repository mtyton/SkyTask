import re

def read_file():
    """
    reads the file
    :return:
    """
    lines = open("skychallenge_accounting_input.txt", "r").readlines()
    return lines


def count_sums(lines):
    """
    takes all readed data, find numbers and sums them
    :param lines:
    :return:
    """
    numbers = []
    new_lines = []
    for line in lines:
        new_lines += (re.findall(r"\-?[\d']+", line))
    for n in new_lines:
        numbers.append(int(n))
    print(sum(numbers))


if __name__ == "__main__":
    data = read_file()
    count_sums(data)