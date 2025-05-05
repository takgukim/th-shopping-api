from dataclasses import dataclass, field

@dataclass
class Product:
    id: int = field(default=0)
    code: str = field(default="")
    name: str = field(default="")