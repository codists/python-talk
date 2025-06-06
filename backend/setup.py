# 使用 setup.py 方便使用完整路径导入，不然导入的时候会报错。示例：
# File "/app/app.py", line 6, in <module>
# python_talk  |     from python_talk.models import User

from setuptools import setup, find_packages

setup(
    name="python_talk",
    version="0.0.1",
    packages=find_packages(),  # This will include `python_talk` and its submodules
)
