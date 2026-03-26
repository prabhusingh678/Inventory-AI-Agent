from openai import OpenAI

client = OpenAI()

def run_agent(query: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an inventory management assistant."},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content