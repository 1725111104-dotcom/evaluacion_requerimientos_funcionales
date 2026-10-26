from ollama import chat

pregunta = input("En qué te puedo ayudar: ")

response = chat(
    model ='llama3.2:3b',
    messages = [
        {   
            'role': 'user',
            'content': f"Responde la siguiente pregunta como si fueras Mario Bros: {pregunta}"
        }
    ],
)
#print(response.message.content)
print(response)