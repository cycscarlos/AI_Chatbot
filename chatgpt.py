import openai
import config

# Usamos la API Key de OpenAI almacenada en la variable api_key ubicada en el archivo ./config.py
openai.api_key = config.api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "¿Cuál es la la misión de OpenAI?"}]
)

# Respuesta completa generada por ChatGPT
# print(response)

# Imprimimos solo la parte correspondiente al mensaje
print(response.choices[0].message.content)
