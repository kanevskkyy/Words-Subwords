class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = list(subwords)  


    def __repr__(self):
        return f"Word: {self.word}, Subwords: {self.subwords}"


    def check_enter_word(self, user_input):
        """check whether the entered word is in subwords"""
        return user_input in self.subwords


    def amount_subwords(self):
        """determine the number of subwords in a word"""
        return len(self.subwords)
