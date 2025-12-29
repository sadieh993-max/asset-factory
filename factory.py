import ollama
import os

# Your Formspree URL goes here!
FORM_URL = "https://formspree.io/f/YOUR_ID_HERE" 

def run_factory():
    # ... (keeping your existing folder logic)
    
    topics = ["Commercial Solar ROI in Texas", "HVAC Maintenance for Warehouses"]
    
    for topic in topics:
        # The prompt now asks for a lead-capture structure
        prompt = f"Write a professional guide about {topic}. End with a 'Next Steps' section."
        
        response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
        content = response['message']['content']

        # THE MAGIC: We append a real HTML form to the bottom of the AI text
        lead_form = f"""
        
        ---
        ## Get a Professional Quote
        Fill out the form below to receive a custom ROI analysis for your business.
        
        <form action="{FORM_URL}" method="POST" style="background: #f4f4f4; padding: 20px; border-radius: 8px;">
          <label>Email:</label><br>
          <input type="email" name="email" required style="width: 100%; margin-bottom: 10px;"><br>
          <label>Company Size:</label><br>
          <input type="text" name="company" style="width: 100%; margin-bottom: 10px;"><br>
          <button type="submit" style="background: #0070f3; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Request Quote</button>
        </form>
        """
        
        full_page = content + lead_form
        
        # Save file logic remains same...
        filename = f"automated_assets/{topic.replace(' ', '_').lower()}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_page)