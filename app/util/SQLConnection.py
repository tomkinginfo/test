from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import os

# DB 連線資訊要透過環境變數給

def get_db():
    db = SQLConnect()

    try:
        yield db
    except Exception:
        db.session.rollback()
        raise
    finally:
        db.close()

class SQLConnect(object):
    def __init__(self) -> None:
        engine = create_engine(f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PWD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_DB")}?charset=utf8mb4')
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        # 這邊須設定資料庫的 table
        self.xxx = Base.classes.xxx
        self.xxxx = Base.classes.xxxx

        self.session = Session(engine)

    def close(self):
        self.session.close()