# 파이썬 3.11 이미지 다운로드 
FROM python:3.11-buster

# 파이썬의 출력 표시를 Docker용으로 조정 
ENV PYTHONUNBUFFERED=1

WORKDIR /src

#pip로 poetry 설치 
RUN pip install "poetry==1.6.1"

#poetry의 정의 파일 복사(존재하는 경우)
COPY pypoject.toml* poetry.lock* ./

#poetry로 라이브러리 설치 (pyproject.toml이 이미 존재하는 경우)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pypoject.toml ]; then poetry install --no-root; fi

#uvicorn 서버 실행
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]