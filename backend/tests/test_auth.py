"""
没啥用的文件，跑一些测试的代码，可以忽略。
"""
import jwt
from datetime import datetime, timedelta

key = 'sssddddd'
token = jwt.encode({'some': 'something', 'iat': datetime.utcnow(),
                    'exp':  datetime.utcnow()+timedelta(seconds=2)}, key, algorithm='HS256')
import time
print(datetime.utcnow()+timedelta(seconds=2))
time.sleep(3)
try:
    de_token = jwt.decode(token, key, algorithms='HS256')
    print(de_token)
except jwt.ExpiredSignatureError:
    print('token  过期')
except jwt.InvalidTokenError:
    print('token 无效')