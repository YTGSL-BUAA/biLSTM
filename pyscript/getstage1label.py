#使用这个py得到一阶段的标签信息，负责提供给bounding box

from scipy.io import loadmat
from scipy.io import savemat
import os
import numpy as np


filepath=r'C:\BUAA\冯如杯代码\data\toGY20200221\myFeaDir'    #一阶段学习的feature的地址


#fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized3D'

fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\boundinglabel'

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
    nump0=np.array(arraylist0)
    tosave=np.empty(nump0.shape,dtype=int)
    for i in range (len(nump0)):
        for j in range(len(nump0[0])):
            for k in range(len(nump0[0][0])):
                if(nump0[i][j][k]>0.5):
                    tosave[i][j][k]=1
                else:tosave[i][j][k]=0
    print(tosave.shape)
    print(' from '+eachpreflix+'\n')
    savemat(os.path.join(fileto,eachpreflix+'_aux'+'.mat'),{'data':tosave})




