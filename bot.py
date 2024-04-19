import gradio as gr
import openai

# Set your OpenAI API key here
openai.api_key = "API KEY"

def chatbot(input_text):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=input_text,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Define the interface for the chatbot using Gradio
input_text = gr.Textbox(lines=7, label="Input Text")
output_text = gr.Textbox(lines=7, label="Output Text")

# Create the interface and launch the chatbot
gr.Interface(fn=chatbot, inputs=input_text, outputs=output_text, title="OpenAI Chatbot").launch()
