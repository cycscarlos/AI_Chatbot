
# : !Hacemos el programa interactivo!
import openai
import config
import typer
from rich import print
from rich.table import Table

# software typer - Manejo de la consola o términal de manera profesionl


def main():

    # Usamos la API Key de OpenAI almacenada en la variable api_key ubicada en el archivo ./config.py

    openai.api_key = config.api_key

    print("[bold red]ChatGPT API con Python[/bold red]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de las aplicación")

    print(table)

    # Definimos el contexto del chat de manera de ir optimizar las preguntas que nos dará (ver role)

    messages = [{"role": "system", "content": "Eres un asistente muy útil"}]

    # Haremos un bucle eterno para las preguntas.. el cual terminará cuando se coloque la palabra clave

    while True:

        # Utilizamos un input para poder chatear  o interactuar

        content = input("¿Sobre que quieres hablar? ")

        if content == 'exit':
            break

    # Una vex que el chat responda, almacenamos las preguntas en el arreglo messages
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        response_content = response.choices[0].message.content

        # Almacenamos las respuestas que nos da Chat GPT, a fin de crear 'contexto' en la conversación, a medida que sigamos haciendo  más preguntas
        messages.append({"role": "assistant", "content": response_content})

    # Respuesta original y completa generada por Chat GPT
    # print(response)

    # ISe imprime solo la parte correspondiente al mensaje de la respuesta
        # print(response.choices[0].message.content)

    # Imprimir la respuesta de la conversación
        print(response_content)


if __name__ == "__main__":
    typer.run(main)
