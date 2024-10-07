class BasicChatbot:
    def __init__(self, name):
        self.name = name
        self.memory = []  # Para guardar el historial de conversaciones

    def greet(self):
        return f"Hola, soy {self.name}. ¿En qué puedo ayudarte hoy?"

    def respond(self, user_input):
        # Verificar si el usuario menciona su nombre
        if "mi nombre es" in user_input.lower():
            user_name = user_input.lower().split("mi nombre es")[-1].strip()
            response = f"¡Encantado de conocerte, {user_name}!"
            self.memory.append(("User", user_input))
            self.memory.append((self.name, response))
            return response

        # Palabras clave para respuestas simples
        keywords = {
            "nombre": "Mi nombre es ChatBot V1. ¿Cuál es el tuyo?",
            "hola": "¡Hola! ¿Cómo te encuentras hoy?",
            "adiós": "¡Hasta luego! Espero verte pronto."
        }

        # Buscar palabras clave en la entrada del usuario
        for word, response in keywords.items():
            if word in user_input.lower():
                self.memory.append(("User", user_input))
                self.memory.append((self.name, response))
                return response

        # Respuesta predeterminada si no se encuentran palabras clave
        response = "No estoy seguro de cómo responder a eso. ¿Puedes intentarlo de otra forma?"
        self.memory.append(("User", user_input))
        self.memory.append((self.name, response))
        return response

    def show_memory(self):
        # Para ver todo el historial de la conversación
        for speaker, message in self.memory:
            print(f"{speaker}: {message}")

def chat():
    print("Bienvenido al chatbot básico. Escribe 'salir' para terminar la conversación.")
    bot = BasicChatbot("ChatBot V1")
    print(bot.greet())

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("ChatBot V1: ¡Adiós! Ha sido un placer hablar contigo.")
            break
        print(f"{bot.name}: {bot.respond(user_input)}")

# Ejecutar el chat en consola
chat()
