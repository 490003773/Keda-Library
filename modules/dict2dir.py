# -*- coding:utf-8 -*-

def dict2dir(src_data):
    result = {}
    try:
        for data in src_data:
            if data["pid"] not in result.keys():
                result[data["pid"]] = []
            result[data["pid"]].append(data)
    except Exception as e:
        print e
        result = {}
    return result
