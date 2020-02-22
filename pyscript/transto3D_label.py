#使用这个py将label转换为3D

from scipy.io import loadmat
from scipy.io import savemat
import os
import numpy as np

#filepath=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized'

filepath=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192LabelAug'


#fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized3D'

fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192LabelAug\3D'

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
    savemat(os.path.join(fileto,eachpreflix+'_seg'+'.mat'),{'data':nump})






