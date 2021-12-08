from  autocorrect import  AutoCorrection
import json

letters = 'ابتثجحخدذرزسشصضطظعغفقكلمنويءؤئإألإ'
ARZ_JSON = './data/ar_arz_wiki_corpus.json'

def get_all_words(file):
    myFile = open(file)
    articles =[]
    for line in myFile:
        article = json.loads(line)
        articles.append(article['text'])

    corpus = ' '.join(articles)
    all_words = corpus.split()
    myFile.close()
    return all_words


word_l = get_all_words(ARZ_JSON)
AC = AutoCorrection(word_l,letters)


while True:
    sentence = input('Please Enter Your Sentence : ')
    words = sentence.split()
    corrected = []
    for word in words:
        best_correct = AC.get_correct(word)
        suggestion = best_correct[0][0]

        corrected.append(suggestion)
        print('suggestion for word {} is {}'.format(word, suggestion))


    print(f'sentence after edit is : '+' '.join(corrected))


