#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine


def run():
    # create_engineを使ってインメモリDBのSQLiteに接続します
    # echo=Trueを指定すると発行されたSQLを標準モジュールのloggingで出力します
    engine = create_engine("sqlite:///:memory:", echo=True)

    # engineはデータベースとのコアインタフェースであり、普段はそのまま使用しない
