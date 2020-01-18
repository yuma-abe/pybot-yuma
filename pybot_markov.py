import random
import pickle

BEGIN='__BEGIN__'
END='__END__'

def generate_text(first_words,first_weight,markov_dict):
    """入力された辞書データをもとに文章を作成する"""
    first_words=random.choices(first_words,weights=first_weight)[0]
    generate_words=[BEGIN,first_words]
    while True:
        pair=tuple(generate_words[-2:])
        word=markov_dict[pair]['words']
        weight=markov_dict[pair]['weight']
        next_word=random.choices(words,weights=weight)[0]
        if next_word==END:
            break
        generate_words.append(next_word)

    return ''.join(generate_words[1:])

def markov_commannd():
    """マルコフ連鎖用の各種データを読み込み、文章を作成する"""
    with open('markov-dict.pickle','rb') as f:
        first_words,first_weight,markov_dict=pickle.load(f)

    return generate_text(first_words,first_weight,markov_dict)