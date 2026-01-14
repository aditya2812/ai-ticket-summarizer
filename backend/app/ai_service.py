import openai
import os
import json

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_ticket(ticket_text: str) -> dict:
    system_prompt = """ You are an expert customer support analyst. 
    Analyze the provided support conversation/chat log and extract a high-level summary.
    
    Format your response as a professional bulleted "AI Overview" with the following points:
    - Who reported the issue and what the core problem was.
    - Who idenitfied the issue.
    - Identification of the root cause or regression. (if the root cause is not yet identified, state that)
    - Actions taken to resolve the immediate issue.
    - Permanent fix status or next steps.
    - Who applied the fix
    
    Respond STRICTLY in JSON format:
    {
        "summary": "- [Point 1]\\n- [Point 2]\\n- [Point 3]\\n- [Point 4]"
    }
    """

    user_prompt = f"Ticket Text: {ticket_text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={ "type": "json_object" }
    )

    response_text = response.choices[0].message.content

    try:
        return json.loads(response_text)
    except (json.JSONDecodeError, IndexError, KeyError):
        return {
            "summary": "- Error parsing AI response. Please try again."
        }
