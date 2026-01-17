"""
作用：
1.开发 API 前的 CRUD 操作。
"""
from sqlalchemy import select

from python_talk.app import create_app
from python_talk.extensions import db
from python_talk.models.menu import Menu


def create_menus(session):
    """
    创建菜单
    """
    root = Menu(url="/", name="home", parent_id=None)
    session.add(root)
    session.commit()
    session.refresh(root)

    # 创建一级子菜单
    users = Menu(url="/users", name="Users", parent_id=root.id)
    products = Menu(url="/products", name="Products", parent_id=root.id)
    orders = Menu(url="/orders", name="Orders", parent_id=root.id)

    session.add_all([users, products, orders])
    session.commit()
    session.refresh(users)
    session.refresh(products)
    session.refresh(orders)

    # 创建二级子菜单（Users 的子菜单）
    user_profile = Menu(url="/users/profile", name="Profile", parent_id=users.id)
    user_settings = Menu(url="/users/settings", name="Settings", parent_id=users.id)

    session.add_all([user_profile, user_settings])
    session.commit()
    session.refresh(user_profile)
    session.refresh(user_settings)

    print(f"[CREATE] root id={root.id}")
    print(f"[CREATE] users id={users.id}, products id={products.id}, orders id={orders.id}")
    print(f"[CREATE] user_profile id={user_profile.id}, user_settings id={user_settings.id}")

    return root.id, users.id, products.id, orders.id, user_profile.id, user_settings.id


def create_menu_production(session):
    """
    生成环境的导航栏
    1.包含字典的列表如何解包：

    """
    menus_data = [
        {"url": "/home", "name": "首页"},
        {"url": "/book", "name": "Python新书速递"},
        {"url": "/login", "name": "登录"},
        {"url": "/register", "name": "注册"},
        {"url": "/reading_reflection", "name": "读后感"},
        {"url": "/reading_reflection_python", "name": "学习路径"},
    ]

    existing_urls = set(
        session.scalars(select(Menu.url)).all()
    )

    new_menus = [
        Menu(**data)
        for data in menus_data
        if data["url"] not in existing_urls
    ]

    if new_menus:
        session.add_all(new_menus)
        session.commit()


def read_menus(session):
    stmt = select(Menu).order_by(Menu.id)
    menus = session.execute(stmt).scalars().all()

    print("[READ] menus:")
    for m in menus:
        print(f"  id={m.id}, name={m.name}, parent_id={m.parent_id}")


def update_menu(session, menu_id: int):
    stmt = select(Menu).where(Menu.id == menu_id)
    menu = session.execute(stmt).scalar_one()

    menu.name = "User Center"
    session.commit()

    print(f"[UPDATE] id={menu.id}, new_name={menu.name}")


def delete_menu(session, menu_id: int):
    stmt = select(Menu).where(Menu.id == menu_id)
    menu = session.execute(stmt).scalar_one()

    session.delete(menu)
    session.commit()

    print(f"[DELETE] id={menu_id}")


def main():
    app = create_app()

    with app.app_context():
        session = db.session

        create_menus(session)
        # create_menu_production(session)
        # update_menu(session, child_id)
        # delete_menu(session, child_id)
        # read_menus(session)


if __name__ == "__main__":
    main()
