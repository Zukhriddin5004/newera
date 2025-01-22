from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.api.controller.products import ProductController
from app.api.dependecies.dependecies import get_user
from app.api.models import Users
from app.api.schemas.auth import User
from app.api.schemas.products import (
    ProductCreateSchema,
    ProductOutSchema,
    ProductUpdateSchema,
)

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/", response_model=List[ProductOutSchema])
async def get_all(
        controller: ProductController = Depends()
):
    return await controller.get_all()

@router.get("/{product_id}", response_model=ProductOutSchema)
async def get_by_id(
        product_id: int,
        controller: ProductController = Depends()
):
    return await controller.get_by_id(product_id)

@router.post("/", response_model=ProductOutSchema, status_code=status.HTTP_201_CREATED)
async def create(
        data: ProductCreateSchema,
        current_user: User = Depends(get_user),
        controller: ProductController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.create(data)

@router.put("/{product_id}", response_model=ProductOutSchema)
async def update(
        product_id: int,
        data: ProductUpdateSchema,
        current_user: User = Depends(get_user),
        controller: ProductController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.update(product_id, data)

@router.delete("/{product_id}")
async def delete(
        product_id: int,
        current_user: Users = Depends(get_user),
        controller: ProductController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.delete(product_id)