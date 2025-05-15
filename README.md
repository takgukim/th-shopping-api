# 🛒 TH 쇼핑몰 운영 API

FastAPI 기반으로 구축된 쇼핑몰 운영 백엔드 API입니다. 제품, 고객 등 쇼핑몰 필수 도메인에 대한 CRUD 기능을 제공합니다. Swagger UI를 통해 직관적인 API 문서 및 테스트가 가능합니다.

---

## 📦 현재 구성된 기능

### ✅ 제품(Product)
- 제품 등록, 수정, 삭제, 조회
- 페이징을 이용한 목록 조회
- 고객이 등록한 제품 관리

### ✅ 고객(Customer)
- 고객 정보 CRUD
- 기타 기능은 추후 구현 예정

---

## 🚧 개발 예정 항목

- 원자재
- 기초정보
- 구매 / 판매
- 포인트
- 게시판
- 통계
- 관리자

---

## 🚀 실행 방법

### 1. Poetry 의존성 설치

```bash
poetry install
```

### 2. 서버 실행

```bash
poetry run uvicorn main:app --reload
```

### 3. Swagger UI 접속

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker 실행 방법

```bash
docker-compose up --build
```

---

## 🧱 프로젝트 구조

```
th-shopping-api/
├── main.py                         # FastAPI 진입점
├── database.py                    # DB 연결 및 세션 관리
├── containers.py                  # 의존성 주입 설정 (Dependency Injection)
├── product/
│   └── interface/controllers/     # 제품 관련 라우터
├── customer/
│   └── interface/controllers/     # 고객 관련 라우터
├── alembic/                       # DB 마이그레이션 (Alembic)
├── pyproject.toml                 # Poetry 프로젝트 설정
├── docker-compose.yml            # 도커 컴포즈 설정
└── ...
```

---

## 📞 문의

- 👤 이태희
- ✉️ developerkimtakgu@gmail.com
