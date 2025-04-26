from containers import Container 

from fastapi import FastAPI

from example.api.router import task
from example.api.router import done

from product.interface.controllers.product_controller import router as product_router

description=""" 

## 제품

제품을 등록,수정,삭제,조회할 수 있다.

* 페이징 기능을 이용해서 조회 할 수 있다.
* **고객이 구매 및 판매하고자 하는 제품**을 등록할 수 있다.
* 제품 수정과 삭제를 할 수 있다.

## 원자재

## 기초정보

## 고객

## 구매

## 판매

## 포인트

## 게시판

## 통계

## 관리자


"""

app = FastAPI(
    title="쇼핑몰 운영을 위한 API",
    summary="쇼핑몰 운영을 위한 제품, 원자재, 기초정보, 고객, 판매, 구매, 포인트, 게시판, 통계, 관리 API 개발한다.",
    description=description,
    contact={
        "name": "이태희",
        "email": "developer@gggg.com",
        "phone": "010-0000-000"
    }
)
app.container = Container()

# 테스트용
app.include_router(task.router)
app.include_router(done.router)

# 제품
app.include_router(product_router)

# 고객