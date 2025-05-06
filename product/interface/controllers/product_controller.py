from dependency_injector.wiring import inject, Provide
from containers import Container

from fastapi import APIRouter, Depends, Query, Path, status, HTTPException

from product.schemas.product_create import ProductCreate 
from product.schemas.product_response import ProductResponse
from product.schemas.product_update import ProductUpdate
from product.schemas.product_list_response import ProductListResponse
from product.schemas.product_update_activate import ProductUpdateActivate
from product.schemas.product_soft_delete import ProductSoftDelete

from product.application.product_service import ProductService

router = APIRouter(prefix="/products")

@router.get(
    "/",
    response_model=ProductListResponse,
    tags=["product"],
    summary="모든 제품 목록 조회",
    description="현재 판매 중인 제품을 조회한다. 삭제는 조회하지 않는다.",
    status_code=status.HTTP_201_CREATED
)
@inject
def get_products(
    start_page: int = Query(1, ge = 1, le = 100, description="페이지 시작번호를 지정하세요"),
    end_page: int = Query(10, ge = 10, le = 10, description="10개 데이터만 조회 가능해요."), 
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductListResponse:
    product_info = product_service.get_products(start_page, end_page)

    return product_info

@router.get(
    "/{product_id}", 
    response_model=ProductResponse, 
    tags=["product"],
    summary="특정 제품 목록 조회",
    description="특정 제품을 조회하며, 판매가 안되는 것은 조회 하지 않는다.",
    status_code=status.HTTP_201_CREATED
)
@inject
def get_product(
    product_id : int = Path(ge = 1, description = "제품의 고유 값"),
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductResponse:
    product = product_service.get_product(product_id)

    return product

@router.post(
    "/",
    response_model=ProductResponse,
    tags=["product"],
    summary="판매하고자 하는 신규 제품을 추가한다.",
    description="중복이 되지 않은 제품의 이름과 코드를 입력한다.현재는 중복되어도 입력된다. 배포 시 개선이 필요하다.",
    status_code=status.HTTP_201_CREATED
)
@inject
def create_product(
    product_body: ProductCreate,
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductCreate:
    
    new_product = product_service.create_product(product_body)

    return new_product

@router.put(
    "/{product_id}", 
    response_model=ProductResponse, 
    tags=["product"],
    summary="특정 제품의 정보를 수정한다.",
    description="현재 존재하는 제품만 수정한다.",
    status_code=status.HTTP_201_CREATED
)
@inject
def update_product(
    product_body: ProductUpdate,
    product_id : int = Path(ge = 1, description = "제품의 고유 값"),
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductResponse:
    update_product = product_service.update_product(product_id, product_body)

    return update_product

@router.patch(
    "/{product_id}/activate", 
    response_model=ProductResponse,
    tags=["product"],
    summary="특정 제품의 판매 및 사용 여부를 변경한다.",
    description="삭제 되지 않는 제품 수정 가능하다",
    status_code=status.HTTP_201_CREATED
)
@inject
def update_product_use_flag(
    activate_body : ProductUpdateActivate,
    product_id : int = Path(ge = 1, description = "제품의 고유 값"),
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductResponse:
    update_product = product_service.update_product_use_flag(product_id, activate_body)

    return update_product

@router.delete(
    "/{product_id}", 
    response_model=ProductResponse,
    tags=["product"],
    summary="특정 제품의 정보를 테이블에서 삭제한다.",
    description="현재 존재하는 제품만 삭제한다.",
    status_code=status.HTTP_201_CREATED
)
@inject
def delete_products(
    product_id : int = Path(ge = 1, description = "제품의 고유 값"),
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductResponse:
    delete_product = product_service.delete_product(product_id)

    return delete_product

@router.post(
    "/{product_id}/soft-delete", 
    response_model=ProductResponse,
    tags=["product"],
    summary="특정 제품의 정보를 완전 삭제 하지 않는다.",
    description="현재 존재하는 제품만 삭제한다.",
    status_code=status.HTTP_201_CREATED
)
@inject
def soft_delete_products(
    soft_delete_body: ProductSoftDelete,
    product_id : int = Path(ge = 1, description = "제품의 고유 값"),
    product_service: ProductService = Depends(Provide[Container.product_service])
) -> ProductResponse:
    
    delete_product = product_service.soft_delete_product(product_id, soft_delete_body)

    return delete_product