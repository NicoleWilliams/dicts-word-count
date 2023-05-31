"""Count words in file."""


# put your code here.


def get_word_count(file_name):
    '''Open a file and prints out how many times each word shows up in the file'''
    
    text_for_counting = open(file_name)

    word_count_dict = {}

    for line in text_for_counting:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict

print(get_word_count("test.txt"))