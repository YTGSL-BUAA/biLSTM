#用来解析ini文件的测试脚本，没什么卵用
import os
import random

file_ini=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized3D'
ini_name='data.ini'

list=[]
ini_file=open(os.path.join(file_ini,ini_name),"r")
for lines in ini_file.readlines():
    list.append(lines.replace("\n",""))
ini_file.close()
random.shuffle(list)

for everyname in list:
    print(everyname)

