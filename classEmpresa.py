# empresa.py
class Empresa:
    def __init__(self):
        self._nombre_empresa = ""
        self._direccion = ""
        self._turno = ""


    # Getter y Setter
    def get_turno(self):
        return self._turno

    def set_turno(self, turno):
        self._turno = turno

    def get_nombre_empresa(self):
        return self._nombre_empresa

    def set_nombre_empresa(self, nombre_empresa):
        self._nombre_empresa = nombre_empresa

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def mostrar_informacion(self):
        return f"Empresa: {self._nombre_empresa}, Dirección: {self._direccion}"
