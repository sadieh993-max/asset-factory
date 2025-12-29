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

# Example High-Ticket Seed Keywords# Updated Seeds for High-Ticket Lead Gen
seeds = [
    "commercial solar tax credits 2025 ",
    "medical malpractice settlement calculator ",
    "industrial hvac maintenance contract cost ",
    "business insurance for trucking companies in ",
    "managed it services pricing for law firms ",
    "corporate wellness program roi for enterprises ",
    "commercial real estate financing rates [City] ",
    "software development outsourcing cost for startups ",
    "permits for luxury adu in [State] "
]

# Execute the harvest
df = harvest_intent(seeds)
df.to_csv("niche_opportunities.csv", index=False)
print("Harvest Complete. File saved as niche_opportunities.csv")