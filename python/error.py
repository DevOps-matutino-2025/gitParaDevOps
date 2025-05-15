class NivelInvalidoError(Exception):
    """Excepción lanzada cuando el nivel proporcionado no es válido"""
    
    def __init__(self, nivel, mensaje="El nivel debe estar entre 1 y 10"):
        self.nivel = nivel
        self.mensaje = mensaje
        super().__init__(f"{mensaje} (Recibido: {nivel})")


def establecer_nivel(nivel):
    if not (1 <= nivel <= 10):
        raise NivelInvalidoError(nivel)
    print(f"Nivel establecido en {nivel}")

#Ejemplo de uso

try:
    establecer_nivel(15)
except NivelInvalidoError as e:
    print(f"Error: {e}")


try:
    establecer_nivel(4)
except NivelInvalidoError as e:
    print(f"Error: {e}")
