import time
from random import choice


class RandomString:

    def __init__(self):
        self.text = None
        self.empty_san = None
        self.points = 0

    def get_random(self, args):
        self.text = choice(args)

    def empty_str(self):
        new_text = []
        for i in self.text:
            new_text.append("_" * len(i))
        self.empty_san = new_text

    def check_letter(self, letter_to_check):
        list_of_index = []
        for word_to_check in self.text:
            count = 0
            for latter in word_to_check:
                if latter == letter_to_check:
                    list_of_index.append(
                        {"word_index": self.text.index(word_to_check), "letter": letter_to_check,
                         "letter_index": count})
                count += 1
        return list_of_index

    def refill_text(self, list_of_index):
        for i in list_of_index:
            self.empty_san[i['word_index']] = self.empty_san[i['word_index']][:i['letter_index']] + i['letter'] + \
                                              self.empty_san[i['word_index']][i['letter_index'] + 1:]

    def done(self):
        for i in self.empty_san:
            if '_' in i:
                return False
        return True

    def check_points(self, list_of_index):
        if not list_of_index:
            self.points -= 1
        else:
            self.points += 5

    def start_game(self, sentences_list):
        self.get_random(sentences_list)
        self.empty_str()
        print(self.text)
        start_game_time = 0
        while not self.done():
            print(" ".join(self.empty_san))
            start_game_time = time.time()
            letter = input("Enter a letter: ")
            self.refill_text(self.check_letter(letter))
            self.check_points(self.check_letter(letter))
        if time.time() - start_game_time <= 30:
            self.points += 100
        print("The game is over. Your score is: " + str(rs.points))


if __name__ == '__main__':
    sentences = [['always', 'be', 'yourself'], ['keep', 'it', 'cool'], ['act', 'as', 'if']]
    rs = RandomString()
    rs.start_game(sentences)
