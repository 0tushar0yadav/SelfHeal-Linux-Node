import subprocess,os
from google import genai
from time import sleep as t



while True:

    #linux:command: tail -n 20 /var/log/syslog
    result = subprocess.run(
        ["tail", "-n", "5", "/var/log/syslog"],
        capture_output=False,
        text=True,
        check=True
    )



    key=os.getenv("GEMINI_API_KEY2")  #gemini api key stored in evironment variable in os
    client = genai.Client(key)

    prompt = f"""
    Task: Analyze the following Linux log buffer and suggest short, actionable fixes.

    Logs:{result}

    Rules:
    - Focus only on errors, failures, and warnings.
    - Keep the summary under 3 bullet points.
    - Provide exact terminal commands to remediate the issues.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        config=types.GenerateContentConfig(
        max_output_tokens=8192  
        )
    )

    buffer=[]

    buffer.append=[response]

    t.sleep(2)

