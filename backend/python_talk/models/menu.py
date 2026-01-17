from typing import Optional

from sqlalchemy import String, ForeignKey, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from python_talk.models.base import PkModel, ModelMixin


class Menu(PkModel, ModelMixin):
    """
    导航栏/菜单栏/分类
    1.一个导航栏下面可以有多个子导航栏
    """
    __tablename__ = 'menu'
    url: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True, comment='url,前端使用')
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True, comment='导航栏名称')
    # Self-Referencing Foreign Key(自引用外键), 参考：https://docs.sqlalchemy.org/en/20/orm/self_referential.html#adjacency-list-relationships
    # 类型注解包含 Optional[],默认情况是 nullable=True
    parent_id: Mapped[Optional[BigInteger]] = mapped_column(BigInteger, ForeignKey('menu.id'), comment='父导航栏ID')
    # 父菜单 1:N 子菜单
    # 因为 Menu 表没有直接定义 id 这个字段，所以不能写成 remote_side=[id]，要写成 remote_side = 'Menu.id'
    parent: Mapped[Optional['Menu']] = relationship('Menu', back_populates='children', remote_side='Menu.id')
    # 所有的子导航栏
    children: Mapped[list['Menu']] = relationship('Menu', back_populates='parent')
    is_visible: Mapped[bool] = mapped_column(Boolean, default=1, index=True, comment='是否展示')
