import os
import re
import subprocess
from google import genai
from google.genai import types
from app import user_input


client = genai.Client()

def myfunc1(ai_query):
    prompt = f"""
    Task: {ai_query}
    Rules:
    - Provide strictly executable bash code.
    - Do not include explanations, notes, or preamble.
    - Output raw commands only without markdown formatting.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=8192
        ),
    )

    raw_code = response.text or ""
    
    # Strip markdown code blocks if the model outputs them
    clean_code = raw_code.strip()
    clean_code = re.sub(r"^```(?:bash|sh)?\r?\n", "", clean_code)
    clean_code = re.sub(r"\r?\n```$", "", clean_code).strip()

    output_filename = "generated_script.sh"

    
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(clean_code + "\n")

    try:
        result = subprocess.run(
            ["bash", output_filename],
            check=True,
            text=True,
            capture_output=True
        )
        print("Execution Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Execution Failed:\n", e.stderr)
    finally:
       
        if os.path.exists(output_filename):
            os.remove(output_filename)


    myfunc1(user_input)