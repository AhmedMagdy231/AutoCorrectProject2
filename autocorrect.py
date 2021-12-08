class AutoCorrection:
    def __init__(self, words_l, alphabets):
        self.word_l = words_l
        self.alphabets = alphabets
        self.vocab = set(self.word_l)
        self.counts = {}
        self.prop = {}
        self.__get_counts()
        self.__get_prop()

    def __get_counts(self):
        for word in self.word_l:
            self.counts[word] = self.counts.get(word, 0) + 1

    def __get_prop(self):
        N = sum(self.counts.values())
        for w, c in self.counts.items():
            self.prop[w] = c / N

    def __transform(self, word):
        delete_l = []
        switch_l = []
        replace_l = []
        insert_l = []

        # delete here
        for i in range(len(word)):
            delete_l.append(word[:i] + word[i + 1:])

        # switch here

        for i in range(len(word)):
            if len(word[i:]) >= 2:
                switch_l.append(word[:i] + word[i + 1] + word[i] + word[i + 2:])
        # replace here

        for i in range(len(word)):
            for w in self.alphabets:
                if len(word) - i >= 1 and w != word[i]:
                    replace_l.append(word[:i] + w + word[i + 1:])

        # insert here

        for i in range(len(word) + 1):
            for w in self.alphabets:
                insert_l.append(word[:i] + w + word[i:])

        return delete_l + switch_l + replace_l + insert_l

    # function that edit one mistake only (delete , switch, insert , replace)

    def __edit_one_mistake(self, word):
        transform = self.__transform(word)
        edit_one_set = set(transform)

        return edit_one_set

    # function that edit Two mistake only (delete , switch, insert , replace)
    def __edit_two_mistake(self, word):
        edit_two_set = set()
        for w in self.__transform(word):
            for w2 in self.__transform(w):
                edit_two_set.add(w2)

        return edit_two_set


    def get_correct(self,word):
        invocab = self.vocab.intersection([word])
        print((invocab))
        print('_________________________________________________________________________________________________')
        edit_1 = self.vocab.intersection(self.__edit_one_mistake(word))
        edit_2 = self.vocab.intersection(self.__edit_two_mistake(word))

        sug_dic = []
        best_sug =[]

        suggestions  = {word : self.prop.get(word,0) for word in invocab or edit_1 or edit_2}
        best_sug = sorted(suggestions.items(),key= lambda item : item[1],reverse=True)[0:2]
        return best_sug


