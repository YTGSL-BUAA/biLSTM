#使用它来正则化原图

from scipy.io import loadmat
from scipy.io import savemat
import os
filefrom=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug'
fileto=r'C:\BUAA\冯如杯代码\data\toGY20200221\somePerson\Resize192ImgAug\normalized'
path=os.listdir(filefrom)

for each_mat in path:
    firstname,secondname=os.path.splitext(each_mat)
    if secondname!= '.mat':
        pass
    else:
        array=loadmat(os.path.join(filefrom,each_mat))
        array=array['data']
        for i in range (len(array)):
            for j in range(len(array[0])):
                if(array[i][j]<0):
                    array[i][j]=0
                elif(array[i][j]>255):
                    array[i][j]=0
        savemat(os.path.join(fileto,each_mat),{'data':array})






