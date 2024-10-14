class WordsFinder:

    def __init__(self, *args):
        self.file_names = []
        for elem in args:
            self.file_names.append(elem)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                line_ent = ''
                for line in file:
                    for char in line:
                        if char not in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                            line_ent += char.lower()
                    line_ent += ' '
            all_words[name] = line_ent.split(' ')
        return all_words

    def find(self, word):
        word = word.lower()
        for key, value in self.get_all_words().items():
            if word in value:
                return {key: value.index(word, 0) + 1}

    def count(self, word):
        word = word.lower()
        for key, value in self.get_all_words().items():
            if word in value:
                return {key: value.count(word)}

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

