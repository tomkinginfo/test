from pydantic import BaseModel
from typing import Any

class OutPutField(BaseModel):
    status: bool # 狀態值， True False
    errmsg: str = None # 錯誤訊息
    data:Any = None
