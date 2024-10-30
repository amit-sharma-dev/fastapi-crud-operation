from typing import Optional, List # Supports for type hints
from pydantic import BaseModel # Most widely used data validation library for python
from enum import Enum # Supports for enumerations

# enum for Gender
class Gender(str, Enum):
    male = "male"
    female = "female"


# enum for Role
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    teacher = "teacher"


class User(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    email_address: str
    phone_number: str
    roles: List[Role]


