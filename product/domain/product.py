from dataclasses import dataclass

@dataclass
class Product:
    id: int = 0
    code: str = ""
    name: str = ""