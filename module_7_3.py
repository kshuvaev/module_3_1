class WordsFinder:
    all_words = {}
    word_find = {}
    word_count = {}

    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):

        for file in self.file_names:
            char_ = (',', '.', '=', '!', '?', ';', ':', ' - ')

            with open(file, 'r', encoding='utf-8') as file_:
                new_str = ''.join([c for c in str(file_.read().lower()) if c not in char_]).split()
            self.all_words[str(file)] = list(new_str)

        return self.all_words

    def find(self, word):
        self.word = word.lower()

        for file in self.file_names:
            i = 0

            for find_word in self.all_words[file]:
                i += 1
                if find_word == self.word:
                    self.word_find[str(file)] = i
                    break
        return self.word_find

    def count(self, word):
        self.word = word.lower()

        for file in self.file_names:
            i = 0

            for find_word in self.all_words[file]:
                if find_word == self.word:
                    i += 1
            self.word_count[str(file)] = i
        return self.word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

#finder1 = WordsFinder('test_file.txt','test_2_file.txt')
#print(finder1.get_all_words())
#print(finder1.find('TEXT'))
#print(finder1.count('teXT'))
