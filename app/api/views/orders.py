from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Sequence

from sqlalchemy.sql.functions import current_user

from app.api.controller.orders import OrderController
from app.api.schemas.orders import OrderCreateSchema, OrderOutSchema, OrderUpdateSchema
from app.api.dependecies.dependecies import get_user
from app.api.schemas.auth import User, UserInSchema

router = APIRouter(prefix="/api/orders", tags=["Orders"])


@router.get("", response_model=List[OrderOutSchema])
async def list_orders(
    current_user: User = Depends(get_user),
    controller: OrderController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.list_orders()


@router.get("/{order_id}")
async def get_order(
    order_id: int,
    current_user: User = Depends(get_user),
    controller: OrderController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return await controller.get_order_details(order_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(
    data: OrderCreateSchema,
    current_user: User = Depends(get_user),
    controller: OrderController = Depends(),
):
    return await controller.create_order(user_id=current_user.id, data=data)


@router.get("/customer/{customer_id}", response_model=Sequence[OrderOutSchema])
async def get_customer_orders(
    customer_id: int,
    current_user: User = Depends(get_user),
    controller: OrderController = Depends(),
):
    if current_user.is_superuser or customer_id == current_user.id:
        return await controller.list_orders_by_user(customer_id)
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@router.get("/{order_id}/status")
async def get_order_status(
    order_id: int,
    current_user: User = Depends(get_user),
    controller: OrderController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    order = await controller.get_order_by_id(order_id)
    return {"order_id": order.id, "status": order.status}

@router.put("/{order_id}")
async def update_order(
    order_id: int,
    data: OrderUpdateSchema,
    current_user: User = Depends(get_user),
    controller: OrderController = Depends(),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403)
    return await controller.update_order_status(order_id, data)