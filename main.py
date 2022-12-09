# fastapi
# uvicorn
# python-multipart
# jinja2

import os

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 실행경로가 다르더라도 정확한 주소를 받기 위해 사용
main_dir = os.path.dirname(__file__)  # 경로를 가져온다.

app = FastAPI()

# 템플릿과 스태틱 파일 가져오기
templates = Jinja2Templates(directory=f"{main_dir}/templates")
app.mount(
    "/static", StaticFiles(directory=f"{main_dir}/static"), name="static")


@app.get("/")  # 최상단 루트 주소
async def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request, "data": "테스트"})  # templates: 20번 라인에서 만든 것 / "request": request 는 꼭 넣기 / 이렇게 서버만 만들면 프론트 엔드가 필요없어진다. 서버만 만들어서 뿌릴 수 있다.
    # 더 알기 위해서 jinja2 문법 검색


@app.post("/result")
async def test(idx: int = Form()):
    return {"idx": idx}


# 패키지 경로를 정확히 하기 위해서 아래방식으로 실행
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) # 이 파일이 있는 경로가 아닌 다른 경로에서 실행하면 "패키지 경로 이탈"이 되어 이렇게 실행 설정
    # uvicorn.run("main:app", reload=True)