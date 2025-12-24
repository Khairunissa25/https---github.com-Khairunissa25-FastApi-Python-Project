from fastapi import FastAPI, HTTPException, Depends
import Services, models, schemas 
from db import get_db,engine
from sqlalchemy.orm import Session

app=FastAPI()   

@app.get("/books/", response_model=list[schemas.Book])
def get_all_books(db:Session=Depends(get_db)):
    return Services.get_book(db)

@app.post("/books/", response_model=schemas.Book)
def create_new_book(book:schemas.BookCreate, db:Session=Depends(get_db)):
    return Services.create_book(db, book)

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id:int, db:Session=Depends(get_db)):
    book_queryset = Services.get_book_by_id(db, book_id)
    if book_queryset:
        return book_queryset
    if not book_queryset:
        raise HTTPException(status_code=404, detail="Book not found")
    
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id:int, book:schemas.BookCreate, db:Session=Depends(get_db)):
    db_update = Services.update_book(db, book_id, book)
    if db_update :
        return db_update 
    if not db_update:
        raise HTTPException(status_code=404, detail="Book not found")
    
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id:int, db:Session=Depends(get_db)):
    db_delete = Services.delete_book(db, book_id)
    if db_delete:
        return db_delete
    if not db_delete:
        raise HTTPException(status_code=404, detail="Book not found")
    
