#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 宣言ベースでテーブルを扱いたい場合、宣言マッピングのベースクラスをdeclarative_base()で作成する
Base = declarative_base()


class User(Base):
    """
    宣言クラスには最低でも __tablename__ と 1つのColumnが必要
    Pythonクラスなので、methodやattributeなども普通に追加できる
    """

    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    fullname: str = Column(String)
    nickname: str = Column(String)


def run():
    print(User.__table__.__repr__())
    """
    Table('users',
          MetaData(bind=None),
          Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
          Column('name', String(), table=<users>),
          Column('fullname', String(), table=<users>),
          Column('nickname', String(), table=<users>),
          schema=None)
"""
