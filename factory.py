import ollama  # pyright: ignore[reportMissingImports]
import os

# 1. Create a home for your assets
folder_name = "automated_assets"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 2. Your "Niche" List (We'll start with these 3 to test)
# Later, you will replace this with your 'niche_opportunities.csv'
topics = [
    "Cost of Commercial Solar in Florida 2025",
    "Permit Requirements for Luxury ADUs in California",
    "ROI of Industrial HVAC Automation for Warehouses"
]

def run_factory():
    print("🚀 Starting the Production Line...")
    
    for topic in topics:
        print(f"✍️ Writing guide for: {topic}...")
        
        # The Master Prompt: This is the 'Secret Sauce'
        prompt = f"""
        Write a high-end professional business report about: {topic}.
        Structure it like this:
        1. Executive Summary
        2. Cost Breakdown Table (Estimate values)
        3. Step-by-Step Implementation Guide
        4. A 'Why Work With Us' section that encourages the reader to request a quote.
        
        Use professional Markdown formatting with headers and bullet points.
        """

        try:
            # Talk to your local Ollama
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            # Save the file
            file_path = os.path.join(folder_name, f"{topic.replace(' ', '_').lower()}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response['message']['content'])
            print(f"✅ Saved to {file_path}")
            
        except Exception as e:
            print(f"❌ Error on {topic}: {e}")

    print("\n🏁 Factory Cycle Complete. Check your 'automated_assets' folder!")

if __name__ == "__main__":
    run_factory()