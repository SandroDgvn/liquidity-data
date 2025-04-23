import pandas as pd

# Données de projection
dates = ["2025-04-30", "2025-05-07", "2025-05-14", "2025-05-21"]
values = [8600, 5200, 6100, 8000]

# Création du DataFrame
df = pd.DataFrame({
    "date": dates,
    "value_usd": values
})

# Export au bon format UTF-8, séparé par virgules
df.to_csv("liquidity.csv", index=False, encoding="utf-8")
print("✅ Fichier liquidity.csv généré.")
