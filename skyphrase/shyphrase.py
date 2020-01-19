def read_file():
    """
    Simplyb reads the file
    :return:
    """
    container = []
    file = open("skychallenge_skyphrase_input.txt", "r").read()
    lines = file.split("\n")
    for line in lines:
        phrases = line.split(" ")
        container.append(phrases)
    return container


def check_phrases(phrases):
    """
    Simply checks phareses
    :param phrases:
    :return:
    """
    used_words = []
    for word in phrases:
        if word in used_words:
            return False
        else:
            used_words.append(word)
    return True


if __name__ == "__main__":
    counter = 0
    words_list = read_file()
    for words in words_list:
        if check_phrases(words):
            counter += 1
    print(counter)