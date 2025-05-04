from dependency_injector.wiring import inject, Provide
from containers import Container

from fastapi import APIRouter, Depends, Query

from  product.schemas import product as product_schema

from product.application.product_service import ProductService

from product.domain.product import Product

router = APIRouter(prefix="/products")

@router.get(
    "/", 
    response_model=list[product_schema.ProductResponse], 
    tags=["product"],
    summary="모든 제품 목록 조회",
    description="현재 판매 중인 제품을 조회한다. 삭제는 조회하지 않는다."
)
@inject
def get_products(
    start_page: int = Query(1, ge = 1, le = 100, description="페이지 시작번호를 지정하세요"),
    end_page: int = Query(10, ge = 10, le = 10, description="10개 데이터만 조회 가능해요."), 
    product_service: ProductService = Depends(Provide[Container.product_service])
):
    products = product_service.get_products(start_page, end_page)
    
    return products

@router.get(
    "/{product_id}", 
    response_model=product_schema.ProductResponse, 
    tags=["product"],
    summary="특정 제품 목록 조회",
    description="특정 제품을 조회하며, 판매가 안되는 것은 조회 하지 않는다."
)
def get_product():
    pass

@router.post(
    "/",
    response_model=product_schema.ProductResponse,
    tags=["product"],
    summary="판매하고자 하는 신규 제품을 추가한다.",
    description="중복이 되지 않은 제품의 이름과 코드를 입력한다.현재는 중복되어도 입력된다. 배포 시 개선이 필요하다."
)
@inject
def create_product(
    product_body: product_schema.ProductCreate,
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> Product:
    new_product = product_service.create_product(
        code=product_body.code,
        name=product_body.name,
    )

    return new_product

@router.put("/{product_id}", response_model=product_schema.ProductResponse, tags=["product"])
def update_product(product_body: product_schema.ProductUpdate):
    pass

@router.delete("/{product_id}", tags=["product"])
def delete_products():
    pass