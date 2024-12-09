import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

# Generate AI insights based on query and data
def generate_insight(invoice_data, query_type):
    # Prepare prompt for AI model (GPT-3 or GPT-4)
    prompt = f"Provide insight for {query_type} related to invoice data: {invoice_data}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
