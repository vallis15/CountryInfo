import tkinter as tk
import requests
import json

def get_country_info():
    country = entry.get()
    url = f"https://restcountries.com/v2/name/{country}"
    response = requests.get(url)
    data = response.json()

    json_output.delete("1.0", tk.END)
    json_output.insert(tk.END, json.dumps(data, indent=4)) 

    if isinstance(data, list):
        data = data[0]  

    capital = data.get("capital", "N/A")
    area = data.get("area", "N/A")
    population = data.get("population", "N/A")
    language = data["languages"][0]["name"] if data.get("languages") else "N/A"
    currency = data["currencies"][0]["name"] if data.get("currencies") else "N/A"

    result = f"Hlavní město: {capital}\n"
    result += f"Rozloha: {area} km²\n"
    result += f"Počet obyvatel: {population}\n"
    result += f"Úřední jazyk: {language}\n"
    result += f"Měna: {currency}"

    text.delete("1.0", tk.END)
    text.insert(tk.END, result)

window = tk.Tk()
window.title("Informace o zemi")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Zjisti", command=get_country_info)
button.pack()

text = tk.Text(window)
text.pack()

json_output = tk.Text(window)
json_output.pack()

window.mainloop()
