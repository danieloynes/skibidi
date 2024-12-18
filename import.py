# import pandas as pd
# # import matplot.pyplot as plt 

# data = pd.read_csv("undersokelse.csv", index_col = 0, skiprows=[0,1], sep=";", na_values=[".", ".."], encoding="latin-1")

# print(data)
# # print(data.head())
# # data.plot()
# # plt.show()

# # Oppgave 1:
# start_tall = int(input("Oppgi et tall for nedtelling: "))
# while start_tall >= 0:
#     print(start_tall)
#     start_tall -= 1
 
# # Oppgave 2:
# tall = int(input("Oppgi et tall for gangetabellen: "))
# for i in range(1, 11):
#     print(f"{tall} x {i} = {tall * i}")
 
# # Oppgave 3
# hemmelig_tall = 42
# print("Gjett et tall mellom 1 og 100!")
# while True:
#     gjett = int(input("Skriv inn ditt gjett: "))
#     if gjett == hemmelig_tall:
#         print("Gratulerer, du gjettet riktig!")
#         break
#     elif gjett < hemmelig_tall:
#         print("For lavt. Prøv igjen.")
#     else:
#         print("For høyt. Prøv igjen.")
 
# # Oppgave 4
# def er_primtall(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return Falser
#     return True
 
# print("Primtall mellom 1 og 100:")
# for tall in range(1, 101):
#     if er_primtall(tall):
#         print(tall)
 
# # Oppgave 5
# def areal_av_sirkel(radius):
#     import math
#     return math.pi * radius ** 2
 
# print("Beregn arealet av sirkler. Skriv 'stopp' for å avslutte.")
# while True:
#     radius_input = input("Oppgi radius: ")
#     if radius_input.lower() == "stopp":
#         break
#     radius = float(radius_input)
#     print(f"Arealet av sirkelen er: {areal_av_sirkel(radius):.2f}")
 
# Oppgave 6
print("Skriv inn tekst. Skriv 'stopp' for å avslutte og se antall ord.")
ord_teller = 0
while True:
    tekst = input("Tekst: ")
    if tekst.lower() == "stopp":
        break
    ord_teller += len(tekst.split())
 
print(f"Totalt antall ord: {ord_teller}")