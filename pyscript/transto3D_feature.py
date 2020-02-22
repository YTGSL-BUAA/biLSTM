#使用这个py将feature文件转换为3D

from scipy.io import loadmat
from scipy.io import savemat
import os
import numpy as np

#filepath=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized'

filepath=r'C:\BUAA\冯如杯代码\data\toGY20200221\myFeaDir'


#fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized3D'

fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\myFeaDir\3D'

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

for eachpreflix in namelist:
    numberlist=[]
    arraylist0=[]
    arraylist1=[]
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
        arraylist0.append(array[0])
        arraylist1.append(array[1])
    nump0=np.array(arraylist0)
    nump1=np.array(arraylist1)
    print(nump0.shape)
    print(' from '+eachpreflix+'\n')
    savemat(os.path.join(fileto,eachpreflix+'_aux'+'_0'+'.mat'),{'data':nump0})
    savemat(os.path.join(fileto,eachpreflix+'_aux'+'_1'+'.mat'),{'data':nump1})







