# TypeIdea
A blog system implemented by [Django](https://www.djangoproject.com/) (deployed on Windows).

## Environment Install
1. Install python 3.6.   
[download link](https://www.python.org/downloads/release/python-360/). For windows user,  you can only download the `Windows x86-64 embeddable zip file`, and then unpack it with a specific folder. e.g. `D:\python-3.6.0-embed-amd64`

2. Create virtual environment   
Change directory to your project folder. e.g `D:/TypeIdea/`    
`virtualenv -p D:\python-3.6.0-embed-amd64\python.exe venv`  
> Note: If the virtualenv doesn't exist in your computer environment, please install it using pip.   
`pip install virtualenv`  

3. Activate virtualenv   
For windows user. Input in termial `./venv/Scripts/activate`   
> Note: Deactivate just input `deactivate` in your terminal.

3. Install django and other packages  
`pip install -r requirements.txt`


## Run server:
## Setup
Create admin account:
```shell
python manage.py createsuperuser
```

Create database and tables:
```shell
python manage.py makemigrations
python manage.py migrate
```

Use dbshell on Windows (Optional):
1. Download `sqlite-tools-win32-x86-*******.zip` on [SQLite Download Page](https://www.sqlite.org/download.html)
2. Unpack it and just paste it to the folder where you have your `manage.py`. You can paste all 3 files there (`sqldiff.exe`, `sqlite3.exe`, `sqlite3_analyzer.exe`).
3. Then: 
    ```shell
    python manage.py dbshell
    sqlite> .tables
    ...
    sqlite> .exit
    ```

## Run
Run server:
```shell
python manage.py runserver
```
Access browser:
```
localhost:8000/super_admin
localhost:8000/admin
```


## Memo
Admin account of author's deployment
- Username: admin
- Password: admin123456
- Email address: 1208571536@qq.com

## References
https://github.com/the5fire/typeidea