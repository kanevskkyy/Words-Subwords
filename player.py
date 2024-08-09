class Player:

    def __init__(self, user_name, *used_words):
        self.user_name = user_name
        self.used_words = list(used_words)


    def __repr__(self):
        return f"Привіт, {self.user_name}!"


    def amount_of_used_word(self):
        """determine the number of subwords used already"""
        return len(self.used_words)


    def add_word(self, new_word):
        """adding a new word used"""
        self.used_words.append(new_word)


    def check_word_not_used(self, word):
        """check if the entered word has not been used before"""
        return word not in self.used_words