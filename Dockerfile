FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# 複製 app 資料夾
COPY ./app /app

# 把 /app 當作根目錄
WORKDIR /app

# 更新 pip
RUN /usr/local/bin/python -m pip install --upgrade pip
# 安裝套件
RUN pip3 install -r requirements.txt
