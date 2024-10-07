# core/incident_manager.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer

class IncidentManager:
    def __init__(self):
        # Carga el modelo y el tokenizer
        self.model_name = "gpt2"  # Puedes elegir otro modelo si lo prefieres
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)

    def generate_incident_report(self, prompt):
        # Codifica el prompt y genera texto
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1)
        report = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return report

    def create_incident(self, incident_description):
        # Genera un informe de incidente a partir de la descripción
        prompt = f"Descripción del incidente: {incident_description}\nInforme del incidente:"
        report = self.generate_incident_report(prompt)
        return report

# Ejemplo de uso
if __name__ == "__main__":
    manager = IncidentManager()
    incident_description = "Se detectó un intento de acceso no autorizado en el servidor."
    report = manager.create_incident(incident_description)
    print(report)
