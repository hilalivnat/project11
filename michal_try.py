
def creat_all_sub_words(words):
    all_sub_words = set()
    for word in words:
        for index in range(1, len(word) + 1):
            all_sub_words.add(word[:index])
    return all_sub_words

