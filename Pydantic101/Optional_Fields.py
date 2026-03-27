from pydantic import BaseModel
from typing import Optional;

class Acnt_User(BaseModel):
    name: str
    age: int
    phone: Optional[str] = None

user6 = Acnt_User(name = "God", age = 25)
print(user6)


