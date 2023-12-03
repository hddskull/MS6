from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4


# class Document:
#     def __init__(self, id: UUID, title: str, body: str):
#         self.id = id
#         self.title = title
#         self.body = body

class Document(BaseModel):
    id: Optional[UUID] = uuid4()
    owner_id: UUID
    title: str
    body: str


class DocumentUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]

