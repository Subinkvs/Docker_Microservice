from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import models
import schemas

from database import engine, get_db


# Create tables
models.Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Product Management API"
)


# CORS

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# -------------------------
# Root
# -------------------------

@app.get("/")
def root():

    return {
        "message": "Product Management API"
    }


# -------------------------
# Get products
# -------------------------

@app.get(
    "/api/products",
    response_model=list[schemas.ProductResponse]
)
def get_products(
    db: Session = Depends(get_db)
):

    return db.query(
        models.Product
    ).all()


# -------------------------
# Get single product
# -------------------------

@app.get(
    "/api/products/{product_id}",
    response_model=schemas.ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.id == product_id
    ).first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# -------------------------
# Create product
# -------------------------

@app.post(
    "/api/products",
    response_model=schemas.ProductResponse
)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product


# -------------------------
# Delete product
# -------------------------

@app.delete(
    "/api/products/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.id == product_id
    ).first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)

    db.commit()

    return {
        "message": "Product deleted successfully"
    }