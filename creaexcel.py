import pandas as pd
import numpy as np
import os

# Crea cartella repo se non esiste
os.makedirs("repo", exist_ok=True)

# Intervallo date
date_range = pd.date_range("2023-01-01", "2023-12-31", freq="D")
n = len(date_range)

# Temperatura: stagionalità + rumore
t = np.arange(n)
temp = 15 + 10*np.sin(2*np.pi*t/365) + np.random.normal(0, 2, n)

# Pioggia: giorni piovosi casuali con quantità gamma
rain_days = np.random.rand(n) < 0.3  # 30% giorni piovosi
rain_amount = np.where(rain_days, np.random.gamma(2, 3, n), 0)

# DataFrame
df = pd.DataFrame({
    "Data": date_range,
    "Temperatura": temp.round(1),
    "Pioggia_mm": rain_amount.round(1)
})

# Salva Excel
df.to_excel("repo/grafici_speciali.xlsx", index=False)
print("File creato: repo/grafici_speciali.xlsx")