import hashlib
import time

md5 = hashlib.sha256()
time_data = []
time = time.gmtime()
time_data.append(time.tm_hour)
time_data.append(time.tm_min)
md5.update(bytes("hello", "utf-8"))
md5.hexdigest()

