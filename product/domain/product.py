from dataclasses import dataclass, field

from datetime import datetime

@dataclass
class Product:
    # 기본값 없음 
    updated_user: str = field(default="")
    updated_datetime: datetime = field(default="")
    deleted_user: str = field(default="")
    deleted_datetime: datetime = field(default="")

    # 기본값 있는건 뒤에 있어야 함
    id: int = field(default=0)
    code: str = field(default="")
    name: str = field(default="")
    price: int = field(default=0)
    usg_flag: int = field(default=0)
    created_user: str = field(default="system")
    created_datetime: datetime =field(default_factory=datetime.now)
    