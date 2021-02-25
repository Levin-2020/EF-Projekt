import time

f = open("countries_copy.svg", "r")
data_raw = f.read()

path_count = data_raw.count("<path")

data = []
ids = {}
id_start = 1000

for i in range(path_count):
    s = data_raw.find("<path")
    e = data_raw.find("</path>")
    temp = data_raw[s:e+7]
    data_raw = data_raw[:s] + data_raw[e+8:]
    data.append(temp)

f_write = open("test.svg", "w")
f_string = ""

for d in data:
    c = d.find("class=")
    if c == -1:
        c1 = d.find("name=")
    if c != -1:
        temp = d[c+7:]
        name = temp[:temp.find("\"")]
    else:
        temp = d[c1+6:]
        name = temp[:temp.find("\"")]

    if name in ids.keys():
        d_id = ids[name]
    else:
        d_id = id_start
        id_start += 1
        ids[name] = d_id
    
    d = d[:-10] + f" onclick=\"click({d_id})\" " + d[-10:]
    f_string += d + "\n"

f_write.write(f_string)


    