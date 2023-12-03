from fastapi import FastAPI, HTTPException
from typing import Optional, List
from app.model.document import Document, DocumentUpdate
from uuid import UUID

# uvicorn main:app --reload
app = FastAPI()

documents: List[Document] = [
    Document(
        id=UUID('febc6a15-b9ad-4e0f-8b67-d8494c277e2b'),
        owner_id = UUID('86f053a0-0dd1-4439-ba43-bdf586220bd2'),
        title="Lorem Ipsum",
        body="ewdfwe"
    ),
    Document(
        id=UUID('54965acc-3798-4a7d-b61d-962ff7d7dbc8'),
        owner_id=UUID('1f4ee684-6856-4a17-8ff2-e0492d3c9099'),
        title="Daft Punk - Around the world",
        body="wefwef"
    )
]


@app.get("/user_docs")
async def fetch_docs():
    return documents

@app.get("/doc_by_id/{owner_id}")
async def fetch_docs(owner_id: UUID):
    for doc in documents:
        if doc.owner_id == owner_id:
            return doc
    return documents

@app.post("/add_doc")
async def add_doc(doc: Document):
    documents.append(doc)
    return {"id": doc.id}
#
#
# @app.delete("/documents/{doc_id}")
# async def delete_doc(doc_id: UUID):
#     for current_doc in documents:
#         if current_doc.id == doc_id:
#             documents.remove(current_doc)
#             return
#     raise HTTPException(
#         status_code=404,
#         detail=f'user with {doc_id} does not exist'
#     )
#
#
# @app.put("/documents/{doc_id}")
# async def update_doc(doc_update: DocumentUpdate, doc_id: UUID):
#     for current_doc in documents:
#         if current_doc.id == doc_id:
#             if doc_update.title is not None:
#                 current_doc.title = doc_update.title
#             if doc_update.body is not None:
#                 current_doc.body = doc_update.body
#             return
#     raise HTTPException(
#         status_code=404,
#         detail=f'user with {doc_id} does not exist'
#     )
