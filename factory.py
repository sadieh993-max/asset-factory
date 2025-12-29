import ollama  # pyright: ignore[reportMissingImports]
import os
import html

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
            
            content = response['message']['content']
            
            # Save the markdown file
            file_path = os.path.join(folder_name, f"{topic.replace(' ', '_').lower()}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Saved to {file_path}")
            
            # Wrap the AI content in HTML so the browser shows the button
            # First escape HTML entities to prevent XSS attacks and broken HTML
            # Then convert newlines to HTML breaks for proper display
            escaped_content = html.escape(content)
            html_content = escaped_content.replace('\n', '<br>')
            
            web_page_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{topic}</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; color: #333; }}
        .form-box {{ background: #f4f7f6; padding: 30px; border-radius: 10px; border: 2px solid #0070f3; margin-top: 50px; }}
        .btn {{ background: #0070f3; color: white; padding: 15px 25px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; font-weight: bold; }}
        .btn:hover {{ background: #0051cc; }}
    </style>
</head>
<body>
    {html_content}
    
    <div class="form-box">
        <h2>Request Your Custom Quote</h2>
        <form action="#" method="POST" onsubmit="handleQuoteSubmit(event)">
            <p>Enter your email to receive the full ROI report and pricing.</p>
            <input type="email" name="email" placeholder="Work Email" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box;">
            <button type="submit" class="btn">GET MY QUOTE</button>
        </form>
    </div>
    
    <script>
        function handleQuoteSubmit(event) {{
            event.preventDefault();
            const email = event.target.querySelector('input[type="email"]').value;
            alert('Thank you! We will contact you at ' + email + ' shortly.');
        }}
    </script>
</body>
</html>
"""
            
            # Save as .html (IMPORTANT)
            html_filename = os.path.join(folder_name, f"{topic.replace(' ', '_').lower()}.html")
            with open(html_filename, "w", encoding="utf-8") as f:
                f.write(web_page_content)
            print(f"✅ Saved HTML to {html_filename}")
            
        except Exception as e:
            print(f"❌ Error on {topic}: {e}")

    print("\n🏁 Factory Cycle Complete. Check your 'automated_assets' folder!")

if __name__ == "__main__":
    run_factory()