from typing import Optional, List
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.products import Product
from app.core.database.config import get_general_session

class ProductRepository:
    def __init__(self, session: AsyncSession = Depends(get_general_session)):
        self.session = session

    async def create(self, **kwargs)->Product:
        product = Product(**kwargs)
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def get_all(self) -> List[Product]:
        result = await self.session.execute(select(Product))
        return result.scalars().all()

    async def find_by_id(self, product_id: int) -> Optional[Product]:
        result = await self.session.execute(select(Product).where(Product.id == product_id))
        return result.scalars().first()

    async def update(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def delete(self, product: Product):
        await self.session.delete(product)
        await self.session.commit()
        return {"message": "Product deleted successfully"}