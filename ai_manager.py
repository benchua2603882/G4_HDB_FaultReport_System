import os
from google import genai
from google.genai import types
from PIL import Image
from pydantic import BaseModel, Field

# 1. Define the exact JSON schema required by your Logic Manager
class FaultReport(BaseModel):
    fault_category: str = Field(description="Must be exactly: plumbing, lift, electrical, or general maintenance")
    summary: str = Field(description="Concise summary of the reported issue")
    risk_indicators: list[str] = Field(description="List of hazards like 'possible electrical exposure'. Empty list if none.")
    is_unclear: bool = Field(description="True if the information is insufficient or cannot be categorized")

# 2. Initialize the client
client = genai.Client()

# 3. Handle the resident's input (Text + Optional Image)
resident_description = "YOO THERE IS A GHOST IN MY CONDO MY BALLS ARE SHIVERING IN THEIR TIMBERS"
image_path = "C:/Users/jkk/.vscode/DevOps Project/G4_HDB_FaultReport_System/ghost.jpg"

contents = [f"Resident description: {resident_description}"]

# Only append the image if it actually exists, satisfying the "(optional)" requirement
if os.path.exists(image_path):
    img = Image.open(image_path)
    contents.append(img)

# 4. Define the AI's role and constraints
system_instruction = """
You are an AI assistant tasked with analyzing maintenance complaints for a condo estate management system. 
Analyze the provided text description and optional image. Extract the core issue and output strictly to the requested schema. 
Do not determine final priority or assign maintenance teams.
"""

# 5. Generate structured content
response = client.models.generate_content(
    model="gemini-3.5-flash-lite", # Use a current multimodal model
    contents=contents,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        response_mime_type="application/json",
        response_schema=FaultReport,
        temperature=0.1, # Low temperature ensures consistent formatting and categorization
    )
)

# The result is guaranteed to be a JSON string matching the FaultReport schema
print(response.text)