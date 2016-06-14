# -*- coding:utf-8 -*-

from conf import db_config

class DatabaseFactory:

    def connection(self):
        obj = __import__(db_config.dbms, {}, {}, [""])
        try:
            obj = __import__(db_config.dbms, {}, {}, [""])
        except ImportError as ipt_error:
            pass
        connect = getattr(obj, db_config.dbclass)
        return connect(db_config)
