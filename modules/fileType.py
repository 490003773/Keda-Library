# -*- coding:utf-8 -*- 
# 判断文件的真实类型
import struct

# 允许的文件类型－文件头
_valid_file_type = {
	"255044462D312E" : "pdf",
	"FFD8FF" 		 : "jpg",
	"89504E47" 		 : "png",
	"424D" 			 : "bmp",
	"3C3F786D6C" 	 : "xml",
	"FF575043" 		 : "wpd",
}

# bytes 转 16进制
def bytes2hex(bytes):
	length = len(bytes)
	hexstr = u""
	for i in range(length):
		t = u"%x" % bytes[i]
		if len(t) % 2:
			hexstr += u"0"
		hexstr += t
	return hexstr.upper()

# 判断文件类型
def file_type(filename):
	# 设置默认返回的类型
	real_type = "unknown"
	# 文件必须已二进制形式读取
	with open(filename, "rb") as f:
		for header in _valid_file_type.keys():
			numBytes = len(header) / 2
			# 每次都要从头开始
			f.seek(0)
			bytesHeader = struct.unpack_from("B"*numBytes, f.read(numBytes))
			hexHeader = bytes2hex(bytesHeader)
			if hexHeader == header:
				real_type = _valid_file_type[header]
				break
	return real_type