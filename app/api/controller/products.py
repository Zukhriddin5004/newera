from fastapi import Depends, HTTPException, status
from app.api.repositories.products import ProductRepository
from app.api.schemas.products import (
    ProductCreateSchema,
    ProductUpdateSchema,
)
from app.api.models.products import Product

class ProductController:
    def __init__(self, product_repository: ProductRepository = Depends()):
        self.product_repository = product_repository

    async def create(self, data: ProductCreateSchema) -> Product:
        product = await self.product_repository.create(**data.model_dump())
        return product

    async def get_all(self):
        return await self.product_repository.get_all()

    async def get_by_id(self, product_id: int) -> Product:
        product = await self.product_repository.find_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    async def update(self, product_id: int, data: ProductUpdateSchema) -> Product:
        product = await self.product_repository.find_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        updated_data = data.model_dump()
        for key, value in updated_data.items():
            setattr(product, key, value)
        return await self.product_repository.update(product)

    async def delete(self, product_id: int):
        product = await self.get_by_id(product_id)
        return await self.product_repository.delete(product)