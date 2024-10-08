class IncidentManager:
    def __init__(self):
        self.incidents = []  # Aquí almacenaremos los incidentes registrados.
        self.hypotheses = []  # Aquí se guardan las hipótesis generadas por la IA.

    def log_incident(self, description):
        """Registra un nuevo incidente basado en una descripción dada."""
        incident = {"description": description, "status": "new"}
        self.incidents.append(incident)
        print(f"[INCIDENT] Nuevo incidente registrado: {description}")
        return incident

    def generate_hypothesis(self, incident):
        """Genera una hipótesis inicial basada en el incidente registrado."""
        hypothesis = f"Podría ser un problema de {incident['description']}"
        self.hypotheses.append(hypothesis)
        print(f"[HYPOTHESIS] Hipótesis generada: {hypothesis}")
        return hypothesis

    def evaluate_hypothesis(self, hypothesis):
        """Evalúa una hipótesis dada con pruebas o análisis (simulado por ahora)."""
        is_valid = True if "problema" in hypothesis else False
        return {"hypothesis": hypothesis, "valid": is_valid}
