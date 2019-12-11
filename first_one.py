#!/usr/bin/env python


prenom = raw_input ("entrez votre prenom : ")
print("Bonjour", prenom)
ville = raw_input ("entrez votre ville : ")
print("Vous venez de", ville)
age = raw_input ("entrez votre age : ")

if age < 20:
    print("Vous etes jeune à ", age, "ans toute la vie devant soi")
else:
    print("Outch", age, "un pied dans la tombe !")

fi

print("Petit resume : ")
print(prenom)
print(ville)
print(age)
