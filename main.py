class VowelFinder:
    vowels = "aeıioöuü"

    def __init__(self, res):
        self.res = res
        self.vowelorconsonant()

    def find(self, rup):
        return rup in self.vowels

    def printoscreen(self, rep, rap):
        print("Vowels: {} \nConsonants: {}".format(rep, rap))

    def vowelorconsonant(self):
        self.vowel = list()
        self.consonant = list()
        for i in self.res:
            if not self.find(i):
                self.consonant.append(i)
            else:
                self.vowel.append(i)
        self.printoscreen(self.vowel, self.consonant)

question = input("Please enter the word you want to test out:\n")
create = VowelFinder(question)
