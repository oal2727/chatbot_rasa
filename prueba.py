import requests

# Define la URL de tu servidor de Rasa
rasa_server_url = "http://localhost:5055/webhook"

while True:
    user_input = input("You: ")

    # Si el usuario ingresa "exit", salimos del bucle
    if user_input.lower() == "exit":
        break

    # Enviar la entrada del usuario al servidor de Rasa
    response = requests.post(rasa_server_url, json={"sender": "user", "message": user_input})

    # Analizar la respuesta del servidor de Rasa
    if response.status_code == 200:
        rasa_response = response.json()

        # Extraer la respuesta del bot de Rasa
        if rasa_response and len(rasa_response) > 0:
            bot_response = rasa_response[0].get("text", "Bot: No se encontró una respuesta.")
            print(f"Bot: {bot_response}")
        else:
            print("Bot: No se encontró una respuesta.")
    else:
        print("Error al comunicarse con el servidor de Rasa.")
