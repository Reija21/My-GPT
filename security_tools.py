import os
import subprocess

class ToolManager:
    def __init__(self, tools_directory):
        self.tools_directory = tools_directory

    def add_tool(self, tool_name):
        print(f"[TOOL MANAGER] Herramienta '{tool_name}' agregada.")

    def evaluate_tool(self, tool_name, test_cases, evaluation_func):
        results = []
        for case in test_cases:
            result = evaluation_func(case)
            results.append({"case": case, "result": result})
        return results

    def clone_repository(self, repo_url, tool_name):
        # Crear la ruta completa para el repositorio
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        repo_path = os.path.join(self.tools_directory, tool_name, repo_name)

        # Crear la carpeta para la herramienta si no existe
        if not os.path.exists(os.path.join(self.tools_directory, tool_name)):
            os.makedirs(os.path.join(self.tools_directory, tool_name))

        # Verificar si la carpeta del repositorio ya existe
        if os.path.exists(repo_path):
            print(f"Error: La carpeta '{repo_path}' ya existe y no está vacía.")
            return

        os.makedirs(repo_path, exist_ok=True)  # Crea la carpeta para el repositorio

        try:
            # Clonar el repositorio
            print(f"Clonando {repo_url} en {repo_path}...")
            subprocess.run(["git", "clone", "-v", "--", repo_url, repo_path], check=True)
            print(f"Repositorio clonado en {repo_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error al clonar el repositorio: {e}")

# Inicializar ToolManager
tools_directory = "Tools"  # Define la carpeta de herramientas
tool_manager = ToolManager(tools_directory)  # Asegúrate de pasar el argumento aquí

# Ejemplo de uso
incident = "tráfico inusual detectado"
print(f"[INCIDENT] Nuevo incidente registrado: {incident}")

hypothesis = "Podría ser un problema de tráfico inusual detectado"
print(f"[HYPOTHESIS] Hipótesis generada: {hypothesis}")
print(f"Evaluación de la hipótesis: {{'hypothesis': '{hypothesis}', 'valid': True}}")

# Agregar una herramienta
tool_name = "detector de OS"
tool_manager.add_tool(tool_name)

# Función de evaluación
def evaluation_func(case):
    return "Linux" in case or "Windows" in case

# Evaluar herramienta (ejemplo)
test_cases = ["TTL indicates Linux", "TTL indicates Windows", "Unknown TTL value"]
tool_evaluation = tool_manager.evaluate_tool(tool_name, test_cases, evaluation_func)
print(f"Evaluación de la herramienta: {tool_evaluation}")

# Clonar un repositorio
repo_url = input("Introduce el enlace de clonación del repositorio: ")
tool_name_input = input("Introduce la carpeta donde deseas guardar el repositorio (ej. Phishing): ")
tool_manager.clone_repository(repo_url, tool_name_input)
