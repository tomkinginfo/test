from pydantic import BaseModel

# pydantic 的 BaseModel 是一個非常好用的資料模組
# 適合用來輸出相同格式資料時候
# 或是接收前端輸入的格式

class InputField(BaseModel):
    name:str=None
    age:int=None
