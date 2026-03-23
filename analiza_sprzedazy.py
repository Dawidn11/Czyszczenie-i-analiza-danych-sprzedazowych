import pandas as pd
df = pd.read_excel("czyste_sprzedaz.xlsx",decimal=",")
pd.set_option("display.max_columns", None)

print(df.head(5))

najczesciej_kupowane = df.groupby("Item")["Quantity"].sum().sort_values(ascending = False).head(5)
print(najczesciej_kupowane)

przychod_z_przedmiotow = df.groupby("Item")["Total Spent"].sum()
print("\nPRZYCHÓD WEDŁUG PRZEDMIOTÓW:")
print(przychod_z_przedmiotow)

laczny_przychod = df["Total Spent"].sum()
print(f"\nŁĄCZNY PRZYCHÓD: {laczny_przychod} zł")

srednia_sprzedaz = df.groupby("Item")["Total Spent"].mean().sort_values(ascending = False)
print("\nŚREDNIA WARTOŚĆ SPRZEDAŻY NA PRODUKT:")
print(srednia_sprzedaz)

liczba_platnosci_karta = (df["Payment Method"] == "Credit Card").sum()
liczba_platnosci_gotowka = (df["Payment Method"] == "Cash").sum()

tabela_platnosci = pd.DataFrame({"Metoda płatności" : ["Credit Card", "Cash"],
                                 "Liczba transakcji" : [liczba_platnosci_karta, liczba_platnosci_gotowka]
                                 })
print("\nZESTAWIENIE METOD PŁATNOŚCI:")
print(tabela_platnosci)

df["Miesiac"] = df["Transaction Date"].dt.to_period("M")
przychod_miesieczny = df.groupby("Miesiac")["Total Spent"].sum().sort_values(ascending = False)

print("\nPRZYCHÓD W PODZIALE NA MIESIĄCE:")
print(przychod_miesieczny)
