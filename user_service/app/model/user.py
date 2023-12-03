from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    student = 'student'
    teacher = 'teacher'

class User(BaseModel):
    id:  Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'roles': self.roles
        }

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    roles: Optional[List[Role]]