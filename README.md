# TypeIdea
A blog system implemented by `Django`.

## Run server:
```shell
cd typeidea
python manage.py runserver
```

## Create admin account
```shell
python managy.py createsuperuser
```

## Use dbshell (on Windows):
1. Download `sqlite-tools-win32-x86-*******.zip` on [SQLite Download Page](https://www.sqlite.org/download.html)
2. Unpack it and just paste it to the folder where you have your `manage.py`. You can paste all 3 files there (`sqldiff.exe`, `sqlite3.exe`, `sqlite3_analyzer.exe`).
3. Then: 
    ```shell
    python manage.py dbshell
    sqlite> .tables
    ...
    sqlite> .exit
    ```
   
## Project admin
- Username: admin
- Password: admin123456
- Email address: 1208571536@qq.com