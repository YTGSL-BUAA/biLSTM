#使用这个py将原图文件转换为3D，并生成ini文件，其中filepath路径下的图片需要已经经过normal_pic.py进行正则化

from scipy.io import loadmat
from scipy.io import savemat
import os
import numpy as np

filepath=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized'



fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized3D'


file_ini_to=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized3D'

ini_name='data.ini'

namelist=[]


path=os.listdir(filepath)
for each_mat in path:
    firstname,secondname=os.path.splitext(each_mat)
    if secondname!='.mat':
        pass
    else:
        temp=''.join(reversed(firstname))
        preflix=''.join(reversed(temp.split('_',1)[1]))
        if(not preflix in namelist):
            namelist.append(preflix)



if(os.path.exists(os.path.join(file_ini_to,ini_name))):
        os.remove(os.path.join(file_ini_to,ini_name))



for eachpreflix in namelist:
    numberlist=[]
    arraylist=[]
    for each_mat in path:
        firstname, secondname = os.path.splitext(each_mat)
        if (secondname != '.mat'):
            pass
        else:
            temp = ''.join(reversed(firstname))
            preflix = ''.join(reversed(temp.split('_', 1)[1]))
            if(preflix==eachpreflix):
                numberlist.append(int(''.join(reversed(temp.split('_',1)[0]))))
    numberlist.sort()
    for number in numberlist:
        str = '%d' % number
        thisfilename=eachpreflix+'_'+str
        array=loadmat(os.path.join(filepath,thisfilename))['data']
        arraylist.append(array)
    nump=np.array(arraylist)
    print(nump.shape)
    print(' from '+eachpreflix+'\n')
    savemat(os.path.join(fileto,eachpreflix+'.mat'),{'data':nump})
    with open(os.path.join(file_ini_to,ini_name),'a')as file_object:
        file_object.write(eachpreflix+'\n')







