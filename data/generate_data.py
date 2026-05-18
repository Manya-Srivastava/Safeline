import pandas as pd
import random

def classify_risk(co, ch4, h2s, o2):
    score = 0
    if co > 150: score += 1
    if ch4 > 3: score += 1
    if h2s > 100: score += 1
    if o2 < 17 or o2 > 25: score += 1

    if score >= 2:
        return "High"
    elif score == 1:
        return "Moderate"
    else:
        return "Low"

data = []
for _ in range(1500):
    co = round(random.uniform(0, 300), 1)
    ch4 = round(random.uniform(0, 10), 2)
    h2s = round(random.uniform(0, 300), 1)
    o2 = round(random.uniform(15, 26), 2)
    
    risk = classify_risk(co, ch4, h2s, o2)
    data.append([co, ch4, h2s, o2, risk])

df = pd.DataFrame(data, columns=["CO", "CH4", "H2S", "O2", "RiskLevel"])
df.to_csv("data/toxic_gas_dataset.csv", index=False)
print("✅ Dataset generated: data/toxic_gas_dataset.csv")
print(df["RiskLevel"].value_counts())
