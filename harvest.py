import requests
import json
import pandas as pd

def harvest_intent(seed_keywords):
    base_url = "http://google.com/complete/search?client=chrome&q="
    results = []

    for keyword in seed_keywords:
        print(f"Harvesting data for: {keyword}")
        response = requests.get(base_url + keyword)
        suggestions = json.loads(response.text)[1]
        
        for s in suggestions:
            # We filter for 'how' or 'cost' to find high-intent buyers
            results.append({"Seed": keyword, "Long_Tail_Query": s})
            
    return pd.DataFrame(results)

# Example High-Ticket Seed Keywords
seeds = [
    "commercial solar installation cost ",
    "how to permit a guest house in ",
    "industrial generator maintenance "
]

# Execute the harvest
df = harvest_intent(seeds)
df.to_csv("niche_opportunities.csv", index=False)
print("Harvest Complete. File saved as niche_opportunities.csv")