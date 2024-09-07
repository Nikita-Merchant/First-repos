def single_root_words(root_word = 'Rus', *other_words):
    same_words = []
    for word_ in other_words:
        if root_word.upper() in word_.upper() or word_.upper() in root_word.upper():
            same_words.append(word_)
    return same_words

#print(single_root_words('Goyda!', 'Go!', 'Goy', 'Da', 'Go', 'Goyda! Ura, Russia!'))
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)