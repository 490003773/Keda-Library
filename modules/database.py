# -*- coding:utf-8 -*-

class Database:

    # initialize database parameters
    def __init__(self, conf):
        pass

    # return a list include some rows(dict(colname=value))
    def query(self, query, *param, **kwparam):
        pass

    # return a row (dict(colname=value))
    def get(self, query, *param, **kwparam):
        pass

    # execute T-SQL like update, delete, insert into
    def execute(self, query, *param, **kwparam):
        pass

    # free database instance
    def __del__(self):
        pass
