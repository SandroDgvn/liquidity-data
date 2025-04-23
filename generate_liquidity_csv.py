import pandas as pd
from datetime import datetime, timedelta

# Dates futures
today = datetime.today()
dates = [(today + timedelta(weeks=i)).strftime("%Y-%m-%d") for i in range(1, 5)]

# Projections fictives
data = {
    "date": dates,
    "central_bank": ["Fed", "ECB", "BoJ", "PBoC"],
    "value_usd": [8600, 5200, 6100, 8000],  # En milliards USD
}

df = pd.DataFrame(data)
df.to_csv("liquidity.csv", index=False)

print("✅ Fichier CSV généré avec succès.")
