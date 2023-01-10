# Import
import random

# Wprowadzenie hasła
lista_hasel = open('hasla.txt', 'r')
hasla_all = lista_hasel.read()
slowa = hasla_all.split('\n')
haslo = (random.choice(slowa).upper())
szubienica = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
proby = len(szubienica)
koniec = proby - 1

# Ilość liter
dlugosc = len(haslo)
current_guess = '_' * len(haslo)
print('Haslo składa się z', dlugosc, 'liter. Jeśli wpiszesz więcej niż jedną literę to zostanie to odczytane jako próba odgadnięcia hasła!\nMasz', proby, 'prób, powodzenia! Hasło:', current_guess)

# Listy
uzyte_litery = []

# Licznik
zle_odp = -1
reszta = proby

# Loop
guess = input('Wpisz literę:\n')
guess = guess.upper()

while zle_odp < koniec and current_guess != haslo:
    if guess in haslo and guess not in uzyte_litery and len(guess) == 1:
        new_guess = ""
        for n in range(dlugosc):
            if guess == haslo[n]:
                new_guess += guess
            else:
                new_guess += current_guess[n]
        uzyte_litery.append(guess)
        current_guess = new_guess
        print('Zgadłeś literę! Twoje hasło:', current_guess, '\nUżyte litery:', uzyte_litery, '\n')
        if current_guess != haslo:
            guess = input('Wpisz literę bądź spróbuj odgadnąć całe hasło:\n')
            guess = guess.upper()
        elif current_guess == haslo:
            print('\n!!!WYGRAŁEŚ!!!\nHasło to:', haslo, '\n!!!GRATULACJE!!!')
            break
    elif guess in uzyte_litery and len(guess) == 1:
        print('Litera', guess, 'została już użyta! Spróbuj ponownie.\n')
        guess = input('Wpisz literę bądź spróbuj odgadnąć całe hasło:\n')
        guess = guess.upper()
    elif len(guess) != 1 and guess != haslo:
        zle_odp += 1
        reszta -= 1
        print('Niestety, podałeś niepoprawne hasło :( \n', szubienica[zle_odp], '\nTwoje hasło:', current_guess, '\nUżyte litery:', uzyte_litery,'\nPozostało prób:', reszta, '\n')
        guess = input('Wpisz literę bądź spróbuj odgadnąć całe hasło:\n')
        guess = guess.upper()
    elif len(guess) != 1 and guess == haslo:
        print('\n!!!WYGRAŁEŚ!!!\nHasło to:', haslo, '\n!!!GRATULACJE!!!')
        break 
    else:
        uzyte_litery.append(guess)
        zle_odp += 1
        reszta -= 1
        if zle_odp != koniec:
            print('Niestety, tym razem Ci się nie udało :( \n', szubienica[zle_odp], '\nTwoje hasło:', current_guess, '\nUżyte litery:', uzyte_litery,'\nPozostało prób:', reszta, '\n')
            guess = input('Wpisz literę bądź spróbuj odgadnąć całe hasło:\n')
            guess = guess.upper()
if zle_odp == koniec:
    print('ZOSTAŁEŚ POWIESZONY \n', szubienica[zle_odp])
    print('Hasło to:', haslo)