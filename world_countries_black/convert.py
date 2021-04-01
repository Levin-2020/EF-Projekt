import time
from deep_translator import GoogleTranslator

import os
os.chdir(r"C:\Users\levin\Desktop\EF-Projekt\world_countries_black")

f = open("world_new.svg", "r")
data_raw = f.read()
path_count = data_raw.count("<path")
print(path_count)
data = []
ids = {}
data_dic = {}
names = []
id_start = 2000

test_output = ""

cnt = 0

for i in range(path_count):
    s = data_raw.find("<path")
    e = data_raw.find("/>",s)
    if s<data_raw.find("title=", s)<e:
        temp = data_raw[s:e+2]
        data_raw = data_raw[:s] + data_raw[e+3:]
        data.append(temp)
    else:
        e = data_raw.find("</path>", s)
        temp = data_raw[s:e+7]
        data_raw = data_raw[:s] + data_raw[e+8:]
        data.append(temp)
for i,d in enumerate(data):
    title = d.find("title=")
    if title != -1:
        s_name = d.find("\"",title)
        e_name = d.find("\"",s_name+1)
        name = d[s_name+1:e_name]
        #name_de = GoogleTranslator('en', 'de').translate(text=name)
        name_de = name
        d = d.replace(name,name_de)
       
        end = d.find("/")

        ids[name_de] = id_start
        id_start += 1

        d = d[:end] + f"onclick=\"click({ids[name_de]})\" " + d[end:]

        data_dic[name_de] = d
        names.append(name_de)

        test_output += d + "\n"
    
    else:
        id_str = d.find("id=")
        s_name = d.find("\"",id_str)
        e_name = d.find("\"",s_name+1)
        name = d[s_name+1:e_name]
        name = name.replace("_", " ")

        ids[name] = id_start
        id_start += 1

        end = d.find(">")

        d = d[:end] + f"\nonclick=\"click({ids[name]})\"" + d[end:]

        data_dic[name] = d
        names.append(name)

        test_output += d + "\n"

test_file = open("test_output1.svg", "w")
test_file.write(test_output)
test_file.close()

geo_csv = ""
svg_csv = ""

for key,item in ids.items():
    geo_csv += f"{ids[key]};{key}\n"

geo = open("geo_test.csv", "w")
geo.write(geo_csv)
geo.close()


