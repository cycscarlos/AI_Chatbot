
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
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del Asistente

    context = {"role": "system",
               "content": "Eres un asistente muy útil"}
    messages = [context]

    # Haremos un bucle eterno para las preguntas.. el cual terminará cuando se coloque la palabra clave

    while True:
        content = __prompt()

        if content == "new":
            print(["💬Nueva conversación creada"])
            messages = [context]
            content = __prompt()

    # Una vex que el chat responda, almacenamos las preguntas en el arreglo messages
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        response_content = response.choices[0].message.content

        # Almacenamos las respuestas que nos da Chat GPT, a fin de crear 'contexto' en la conversación, a medida que sigamos haciendo  más preguntas
        messages.append({"role": "assistant",
                         "content": response_content})

    # Imprimir la respuesta de la conversación
        print(f"[blue]{response_content}[/blue]")

# Definimos una función ue se encargará de manejar el tema de la salida del chat


def __prompt() -> str:

    prompt = typer.prompt("\n¿Sobre que quieres hablar? ")

    if prompt == 'exit':

        exit = typer.confirm("¿Estás seguro?")
        print(["Hasta Luego"])
        if exit:  # es un booleano (y/n)
            raise typer.Abort()

        return __prompt()  # sino quiere salir, hacemos el ciclo de nuevo

    return prompt


if __name__ == "__main__":
    typer.run(main)
