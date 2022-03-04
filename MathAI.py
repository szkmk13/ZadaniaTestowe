from numpy import *


class Neural_Network:
    def __init__(self):
        random.seed(1)
        self.weights = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * dot(inputs.T, error)
            self.weights += adjustment

    def think(self, inputs):
        return dot(inputs, self.weights)


neural_network = Neural_Network()
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = array([[10, 4, 14, 30]]).T
neural_network.train(inputs, outputs, 10000)
print(neural_network.think(array([15, 2])))


def letter_couter(word):
    dictionary = {}
    for letter in word:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    print(dictionary)
    maks=max(dictionary.values())
    print(maks)
   
    for i in range(maks)


letter_couter("""1. O, radości, iskro bogów,
kwiecie Elizejskich Pól,
święta, na twym świętym progu staje
nasz natchniony chór.
Jasność twoja wszystko zaćmi,
złączy, co rozdzielił los.
Wszyscy ludzie będą braćmi tam,
gdzie twój przemówi głos.
2. Patrz, patrz, wielkie słońce światem biegnie,
sypiąc złote skry.
Jak zwycięzca i bohater biegnij,
bracie tak i ty.
Radość tryska z piersi Ziemi,
radość pije cały świat.
Dziś wchodzimy, wstępujemy
na radości złoty ślad.
3. Ona w sercu, w zbożu, w śpiewie,
ona w splocie ludzkich rąk.
Z niej najlichszy robak czerpie,
w niej największy nieba krąg.
Wstańcie ludzie, wstańcie wszędzie,
ja nowinę niosę wam.
Na gwiaździstym firmamencie
bliska radość błyszczy nam.
""")