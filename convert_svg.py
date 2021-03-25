import time

f = open("countries_copy.svg", "r")
data_raw = f.read()

path_count = data_raw.count("<path")

data = []
ids = {}
data_dic = {}
id_start = 1000

for i in range(path_count):
    s = data_raw.find("<path")
    e = data_raw.find("</path>")
    temp = data_raw[s:e+7]
    data_raw = data_raw[:s] + data_raw[e+8:]
    data.append(temp)

f_write = open("test.svg", "w")
f_string = ""

countries_csv = ""
svg_csv = ""
geo_csv = ""

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
    d = d.replace("\n","")
    if name in data_dic:
        data_dic[name] += d
    else:
        data_dic[name] = d


for key in ids.keys():
    svg_csv += str(ids[key]) + "," + data_dic[key] + "," + f"A country called {key}" + "," + "2" + "," + str((ids[key])) + "\n"
    geo_csv += str(ids[key]) + "," + f"{key}" + "," + "country" + "\n"


ff = open("svg.csv", "w")
ff.write(svg_csv)
ff.close()

ff = open("geo_elements.csv", "w")
ff.write(geo_csv)
ff.close()
#f_write.write(f_string)