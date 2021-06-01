class Logique:
    def __init__(self):
        self.number = [
            0, 1, 2, 3, 4, 5, 6, 7, 8,
            9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19,  20, 30, 40, 50, 60, 70,
            80, 90]
        self.alpha = [
            'zero', 'un', 'deux', 'trois', 'quatre', 'cinq',
            'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze',
            'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf', 'vingt',
            'trente', 'quarante', 'cinquante', 'soixante', 'septente',
            'quatre-veingt', 'nonente']

        self.exceptes = [
            10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 30, 40, 50, 60, 70,
            80, 90
        ]
        # initialisation du dictionnaire
        self.dicos = {}

    def saisir(self):
        entry = int(input())
        return entry

    def diction(self):
        for i in range(len(self.alpha)):
            self.dicos[int(self.number[i])] = self.alpha[i]
        return self.dicos

    def deux(self, num):
        b = str(num)
        value1 = self.diction()[(int(b[0])*10)]
        value2 = self.diction()[int(b[1])]
        if value2 != 'un' and value2 != 'zero':
            chaine = f'{value1} {value2}'
            return chaine
        elif value1 == 'zero':
            if value2 == 'zero':
                chaine = 'zero'
                return chaine
            else:
                chaine = self.kernel(int(b[1]))
                return chaine
        else:
            chaine = f'{value1} et {value2}'
            return chaine

    def trois(self, numb):
        # cas à verifier si 100 - 900
        bn = str(numb)
        value1 = self.diction()[int(bn[0])]
        value2 = self.diction()[int(bn[1])]
        value3 = self.diction()[int(bn[2])]
        back_number = int((bn[1]) + (bn[2]))
        # traitons le cas de cent
        if value1 == 'un':
            if value2 == 'zero' and value3 == 'zero':
                chaine = 'cent'
                return chaine
            elif value2 == 'zero' and value3 != 'zero':
                chaine = f'cent et {value3}'
                return chaine
            elif value2 != 'zero' and (value3 == 'zero' or value3 != 'zero'):
                inter = self.kernel(back_number)
                chaine = f'cent {inter}'
                return chaine
        elif value1 == "zero":
            tak = self.deux(back_number)
            return tak
        elif value1 != 'zero' and value1 != 'un':
            if value2 == 'zero' and value3 == 'zero':
                chaine = f'{value1} cents'
                return chaine
            elif value2 == 'zero' and value3 != 'zero':
                chaine = f'{value1} cent et {value3}'
                return chaine
            elif value2 != 'zero' and (value3 == 'zero' or value3 != 'zero'):
                inter = self.kernel(back_number)
                chaine = f'{value1} cent {inter}'
                return chaine

    def quatre(self, nu):
        bn = str(nu)
        value1 = self.diction()[int(bn[0])]
        value2 = self.diction()[int(bn[1])]
        value3 = self.diction()[int(bn[2])]
        value4 = self.diction()[int(bn[3])]
        back_number = int((bn[1]) + (bn[2]) + (bn[3]))
        if value1 == 'un':
            if value2 == 'zero' and value3 == 'zero' and value4 == 'zero':
                chaine = 'mille'
                return chaine
            if value2 == 'zero' and value3 == 'zero' and value4 != 'zero':
                chaine = f'mille {value4}'
                return chaine
            elif value2 != 'zero' or value2 == 'zero':
                inter = self.kernel(back_number)
                return f'mille {inter}'
        elif value1 == 'zero':
            tak = self.kernel(back_number)
            return tak
        elif value1 != 'zero' and value1 != 'un':
            if value2 == 'zero' and value3 == 'zero' and value4 == 'zero':
                chaine = f'{value1} milles'
                return chaine
            elif value2 == 'zero' and value3 == 'zero' and value4 != 'zero':
                chaine = f'{value1} milles {value4}'
                return chaine
            elif value2 != 'zero' or value2 == 'zero':
                inter = self.kernel(back_number)
                return f'{value1} mille {inter}'

    def kernel(self, number):
        # changeons  le type de la variable
        number_str = str(number)
        # si le nombre donner est une seule caractere
        if len(number_str) == 1:
            tek = self.diction()[number]
            return tek
        # si le nombre donner est duex caracter
        elif len(number_str) == 2:
            if number in self.exceptes:
                tek = self.diction()[number]
                return tek
            else:
                return self.deux(number)
        elif len(number_str) == 3:
            return self.trois(number)
        elif len(number_str) == 4:
            return self.quatre(number)
        else:
            chaine = 'valeur non prise en charge'
            return chaine
