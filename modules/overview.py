# -*- coding:utf-8 -*-
import os, time
import platform
from modules import CommonCategory, Common, Book, Topic, Magazine, DatabaseFactory

def dir_size(dir):
    size = 0L
    for root, dirs, files in os.walk(dir):
        size += sum(\
                [os.path.getsize(os.path.join(root, name)) \
                for name in files] \
            )
    return size

def db_size():
    query = "SELECT sum(DATA_LENGTH)+sum(INDEX_LENGTH) as total \
            FROM information_schema.TABLES \
            WHERE TABLE_SCHEMA='ikeda_library'"
    row = DatabaseFactory().connection().get(query)
    return row["total"]

def count():
    record = {"count":0}
    for c in ["Book", "Common", "Topic", "Magazine"]:
        record[c] = globals()[c]().count()["cnt"]
        record["count"] += record[c]
    return record

def overview(path, conf):
    # 系统运行时间，单位秒
    run_time = 0.0
    with open("/proc/uptime", "r") as t:
        run_time = t.read()
    run_time = float(run_time.split(" ")[0])
    # 文档路径
    file_dir = os.path.join(path, "file")
    # 文档大小
    file_size = dir_size(file_dir)/1024/1024
    # 获取本地ip
    ip = os.popen("/sbin/ifconfig | grep 'inet addr' | awk '{print $2}'").read()
    lib_info = dict(
        count = count(),
        ip = ip[ip.find(':')+1:ip.find('\n')],
        file_dir = file_dir,
        file_size = file_size,
        system = "-".join(platform.linux_distribution()),
        server_name = "科达文库",
        db_size = db_size()/1024/1024,
        rtime = "%ss" %run_time
    )
    return lib_info
