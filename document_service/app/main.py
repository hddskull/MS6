from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List, Annotated
from uuid import UUID
from app.model.document import Document, DocumentUpdate
from sqlalchemy.orm import Session
import app.db.database as database

# uvicorn main:app --reload
app = FastAPI()
database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/user_docs")
async def fetch_docs(db: db_dependency):
    result = db.query(database.DBDoc).offset(0).limit(100).all()
    return result

@app.get("/doc_by_id/{owner_id}")
async def fetch_docs(owner_id: UUID, db: db_dependency):
    result = db.query(database.DBDoc).filter(database.DBDoc.owner_id == owner_id).first()
    print(owner_id)
    print(result)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f'doc with such owner id is not found. owner_id: {owner_id}'
        )
    return result


@app.post('/add_doc')
async def add_doc(doc: Document, db: db_dependency):
    db_doc = database.DBDoc(
        id=doc.id,
        owner_id=doc.owner_id,
        title=doc.title,
        body=doc.body,
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)


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
