# @Filename: base.py
# @Author: codists
# @Created: 2025-07-14 23:13:17
import datetime as dt

from python_talk.extensions import db

__all__ = ['Model', 'PkModel', 'ModelMixin']


class Model(db.Model):
    __abstract__ = True

    def __iter__(self):
        for c in self.__table__.columns:
            yield c.name, getattr(self, c.name)


class PkModel(Model):
    """Abstract model class which has primary key

    """
    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)
    create_time = db.Column(db.DateTime, default=dt.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, comment='更新时间')

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        if commit:
            db.session.commit()
        else:
            db.session.flush()
        return instance

    @classmethod
    def update(cls, id_: int, **kwargs):
        instance = cls(id=id_, **kwargs)
        db.session.merge(instance)
        db.session.commit()
        return cls.query.get(id_)

    @classmethod
    def delete(cls, id_: int):
        cls.query.filter_by(id=id_).delete()
        db.session.commit()


class ModelMixin(object):
    """为 model附加各种功能

    :return: None
    """

    def __iter__(self):
        for c in self.__table__.columns:
            yield (c.name, getattr(self, c.name))
