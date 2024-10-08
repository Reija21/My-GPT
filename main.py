# main.py

from incident_manager import IncidentManager
from security_tools import ToolManager

# Inicializar los módulos.
incident_manager = IncidentManager()
tool_manager = ToolManager()

# Registrar un incidente.
incident = incident_manager.log_incident("tráfico inusual detectado")

# Generar y evaluar hipótesis.
hypothesis = incident_manager.generate_hypothesis(incident)
evaluation = incident_manager.evaluate_hypothesis(hypothesis)
print(f"Evaluación de la hipótesis: {evaluation}")

# Agregar una herramienta de ejemplo al ToolManager.
tool_manager.add_tool("detector de OS", lambda x: "Linux" in x or "Windows" in x)

# Evaluar la herramienta con casos de prueba.
test_cases = ["TTL indicates Linux", "TTL indicates Windows", "Unknown TTL value"]
tool_evaluation = tool_manager.evaluate_tool("detector de OS", test_cases)
print(f"Evaluación de la herramienta: {tool_evaluation}")

# Usar la herramienta en un ejemplo.
tool_output = tool_manager.run_tool("detector de OS", "TTL indicates Linux")
print(f"Resultado de la herramienta: {tool_output}")

# Clonar un repositorio
repo_url = input("Introduce el enlace de clonación del repositorio: ")
directory = input("Introduce la carpeta donde deseas guardar el repositorio (ej. Phishing): ")
tool_manager.clone_repository(repo_url, directory)
