from fastapi import APIRouter, BackgroundTasks, Depends

# 匯入演算法
from routers.example.service import somelogic

# 匯入 schemas
from routers.example import schemas

# 統一的輸出格式
from util.alloutputfield import OutPutField

# 讀取 DB
from util.SQLConnection import get_db

from sqlalchemy.orm import exc

router = APIRouter()

@router.get("/", tags=["Example"], summary="取得數據")
def example_get():
    """取得數據
    """
    return {"example": 1}

# 使用 OutPutField 當作輸出格式模組
@router.get("/2", tags=["Example"], summary="取得數據", response_model=OutPutField)
def example_get2():
    """取得數據
    """
    return {"status":True, "data":[{"example": 1}]}

def test_background():
    """這是可以responce之後做的事情
    """
    print("do something")

@router.get("/taskbackground", tags=["Example"], summary="測試 taskbackground", response_model=OutPutField)
def example_taskground(bk: BackgroundTasks):
    """測試 taskbackground
    """
    bk.add_task(test_background)
    return {'status': True}

@router.get("/logic", tags=["Example"], summary="執行一些演算法", response_model=OutPutField)
def example_logic():
    """執行一些演算法
    """
    somelogic.do_some_logic()
    return {"status": True}

@router.post("/schemas", tags=["Example"], summary="接收 post 的資料", response_model=OutPutField)
def example_schemas(inputs:schemas.InputField):
    """接收 post 的資料
    """
    return {
        "status": True,
        "data": {"msg": "very good!"}
    }

@router.get("/exception", tags=["Example"], summary="當程式內拋出現錯誤", response_model=OutPutField)
def example_exception():
    """當程式內拋出現錯誤
    """

    # 會統一由 main.py unknown_exception_handler 處理
    raise Exception("哎呀~出錯啦~")

    return {
        "status": True,
        "data": {"msg": "very good!"}
    }
 
@router.get("/db", tags=["Example"], summary="讀取 DB 資訊", response_model=OutPutField)
def example_db(db=Depends(get_db)):
    """ 讀取 DB 資訊

    事前工作:
        先在 mysql 上面先手動建立好 table 和 schema，程式內就不需要設定 model 那些

    新增/查詢/更新/刪除 方法可以 google "python sqlalchemy" 的操作，或是看下面範例

    """

    # 讀取某 table 全部資料
    # dblist = db.session.query(db.menbers).all()

    # 查詢條件
    # dblist = db.session.query(db.xxxx).filter_by(name="johnny").all()

    # 只取得一筆，沒有資料為 None
    # dbitem = db.session.query(db.xxxx).filter_by(name="johnny").first()

    # 更新資料
    # dbitem.name = "johnny 2"
    # db.session.commit()

    # 更新時引發錯誤狀況
    # try:
    #     dbitem.name = "johnny 2"
    #     db.session.commit()
    # except (exc.IntegrityError, exc.DataError) as e:
    #     db.session.rollback()
    #     raise Exception("資料更新錯誤!")

    return {"status": True}