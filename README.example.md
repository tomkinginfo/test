# <功能名稱>

## 目錄

這邊可以使用 vscode 外掛模組 `Markdown All in One` 的 `Table of contents` 自動產生

操作方法:

1. 按下 `ctrl`+`shift`+`p`
2. 輸入 `create table of contents`
3. 按下 `enter` 即可自動產出

- [<功能名稱>](#功能名稱)
  - [目錄](#目錄)
  - [大綱](#大綱)
  - [主機資訊](#主機資訊)
    - [AWS EC2](#aws-ec2)
    - [AWS Aplify](#aws-aplify)
    - [AWS codedeploy](#aws-codedeploy)
    - [redis](#redis)
    - [env 環境變數](#env-環境變數)
  - [API 說明](#api-說明)
  - [DB](#db)
    - [RDS](#rds)
  - [DB schema 說明](#db-schema-說明)
    - [<某 table>](#某-table)
  - [測試](#測試)
    - [pytest](#pytest)
  - [Deploy 部屬](#deploy-部屬)
    - [流程](#流程)

## 大綱

<說明這個API的功能是甚麼>

## 主機資訊

<可能會使用到 AWS 那些功能>

### AWS EC2

<如果有的話>

- Name: `<ec2 名稱>`
- IP: <外部IP>
- Tag 資訊:
  - description: <說明>
- Keypair: <使用甚麼pem登入>

### AWS Aplify

<如果有的話>

- application name: ?
- enviroment: ?

### AWS codedeploy

<如果有的話>

- application-name: `<name>`
- deployment-group-name: `<deploy name>`

### redis

<如果有的話>

host: `<host>`

### env 環境變數

程式內使用到的環境變數名稱

- DB_DB
- DB_HOST
...

## API 說明

可以於瀏覽器輸入 `/docs` 查閱相關資訊

## DB

有使用到哪些資料庫

### RDS

- host: `<host url>`
- user: `<user name>`

> 這邊不放 PWD

以此類推....

## DB schema 說明

### <某 table>

field | type | 說明
------|------|---
name  | str  | 名稱

以此類推...

## 測試

<這邊說明如何在本機執行>

範例:

打開 vscode 對 `main.py` 按下 `F5`

### pytest

放置於 `app/tests` 底下

## Deploy 部屬

<如果有AWS後，這邊會說明怎麼從本機電腦操作到AWS主機上>

### 流程

1. 本機 local 修改程式後
2. 執行 pytest 的部分都正常
3. git push master 到 github
4. github 的 actions workflow(.github/workflow/main.yml)
5. aws codedeploy(appspec.yml)
6. aws ec2 主機(deploy.sh)

