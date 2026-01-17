# @Filename: __init__.py
# @Author: codists
# @Created: 2025-07-14 23:04:11

# 因为 Book 模型实在另外一个项目 booksbot 用，alembic 检测不到，所以导入到这里，让 alembic 检测到
from .user import User
from .book import Book
from .menu import Menu