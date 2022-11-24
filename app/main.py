import uvicorn
import sys
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import RequestValidationError
from util.alloutputfield import OutPutField
from routers.example import urls as example
from loguru import logger
import settings

description = """
## 功能說明

這邊可以寫這個API是支援甚麼服務 test auto
"""

app = FastAPI(
    title="<自定義服務名>",
    description=description,
    version="3.2.1",
    contact={
        "name": "<Johnny>",
        "email": "<johnnytan@kingsinfo.com.tw>",
    },
)

# 先刪除所有logger，再新增一個level等級的
logger.remove()
logger.add(sys.stdout, level=settings.LOGGER)

# 偵測全域的錯誤資訊
@app.exception_handler(Exception)
def unknown_exception_handler(request: Request, exc: Exception):
    """
    Catch-all for all other errors.
    """
    return ORJSONResponse(
        status_code=200, 
        content=OutPutField(
            status=False,
            errmsg=str(exc)
        ).dict()
    )

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    """處理 request 資料沒給或給錯的狀況
    """
    _h = lambda err: ".".join(err['loc']) + " is " + err['msg'] + " and " + err['type']
    msg = [_h(err) for err in exc.errors()]
    return ORJSONResponse(
        status_code=200, 
        content=OutPutField(
            status=False,
            errmsg=", ".join(msg)
        ).dict()
    )

# 基本的 get 用法
@app.get("/", tags=['分類1'])
def hello_world():
    """這邊可以寫 API 的說明aaaaaaaaacccccccc
    """
    return {"status": True}

# 使用 OutPutField 當作輸出格式模組
@app.get("/2", tags=['分類1'], response_model=OutPutField)
def hello_world2():
    """這邊可以寫 API 的說明
    """
    return {"status": True}

# 包含 param 的 get 用法
# get /user?user=johnny
# get /user?user=johnny&age=30
@app.get("/user", tags=['分類1'])
def get_user(user:str=None, age:int=None):
    """直接顯示 user 和 age 資料

    Args:
        user (str, optional): 名稱. Defaults to None.
        age (int, optional): 年紀. Defaults to None.

    """
    return {"Hello": user, "age": age}

# 使用 OutPutField 當作輸出格式模組
@app.get("/user2", tags=['分類1'], response_model=OutPutField)
def get_user2(user:str=None, age:int=None):
    """直接顯示 user 和 age 資料

    Args:
        user (str, optional): 名稱. Defaults to None.
        age (int, optional): 年紀. Defaults to None.

    """
    return {"status": True, "data": {"Hello": user, "age": age}}

# 註冊 example
app.include_router(
    example.router, 
    prefix="/example", # 並基於 /example
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True, debug=True)
