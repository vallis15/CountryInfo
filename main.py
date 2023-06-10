import tkinter as tk
import requests


def get_country_info():
    country = entry.get()
    url = f"https://restcountries.com/v2/name/{country}"
    response = requests.get(url)
    data = response.json()[0]

    capital = data["capital"]
    area = data["area"]
    population = data["population"]
    language = data["languages"][0]["name"]
    currency = data["currencies"][0]["name"]

    result = f"Hlavní město: {capital}\n"
    result += f"Rozloha: {area} km²\n"
    result += f"Počet obyvatel: {population}\n"
    result += f"Úřední jazyk: {language}\n"
    result += f"Měna: {currency}"

    text.delete("1.0", tk.END)
    text.insert(tk.END, result)


# Vytvoření okna
window = tk.Tk()
window.title("Informace o zemi")

# Vytvoření vstupního pole
entry = tk.Entry(window)
entry.pack()

# Vytvoření tlačítka
button = tk.Button(window, text="Zjisti", command=get_country_info)
button.pack()

# Vytvoření textového pole pro výstup
text = tk.Text(window)
text.pack()

# Spuštění smyčky událostí GUI
window.mainloop()
