from .base import *


# 因为将settings.py拆分成settings文件包, 导致获取的源码根目录不正确, 这里进行修正.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True

# 重新导入数据库配置, 不然db.sqlite3依旧在错误的文件目录生成.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
