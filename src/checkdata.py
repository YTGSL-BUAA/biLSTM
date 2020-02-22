# 这个文件用于确认所有的输入数据合法


from utility.ini_file_io import load_train_ini
from scipy.io import loadmat
import os
tr_ini_file = '../outcome/model/ini/tr_param.ini'
param_Levels = load_train_ini(tr_ini_file)
level_N = len(param_Levels)
ini_name = 'data.ini'
for s in range(1):
    print('============= checking data=============')
    dict_s = param_Levels[s]
    list = []
    ini_file = open(os.path.join(dict_s['data_ini'], ini_name), "r")
    for lines in ini_file.readlines():
        list.append(lines.replace("\n", ""))
    ini_file.close()
    allright=True
    for i in range(len(list)):
        sample_idx=list[i]
        print('checking '+str(i+1)+' of '+str(len(list)))
        thisright=True
        file_sfix = '_aux.mat'
        aux_path = os.path.join(dict_s['img_b_path'], (str(sample_idx) + file_sfix))
        aux_c0_path = os.path.join(dict_s['img_bm_path'], (str(sample_idx) + "_aux_" + str(0) + ".mat"))
        aux_c1_path = os.path.join(dict_s['img_bm_path'], (str(sample_idx) + "_aux_" + str(1) + ".mat"))
        file_sfix = '.mat'
        us_path = os.path.join(dict_s['img_a_path'], (str(sample_idx) + file_sfix))
        file_sfix = '_seg.mat'
        targ_path = os.path.join(dict_s['seg_c_path'], (str(sample_idx) + file_sfix))
        aux=loadmat(aux_path)['data']
        aux_c0=loadmat(aux_c0_path)['data']
        aux_c1=loadmat(aux_c1_path)['data']
        us=loadmat(us_path)['data']
        targ=loadmat(targ_path)['data']
        if(not(aux.shape==aux_c0.shape==aux_c1.shape==us.shape==targ.shape)):
            print('fatal error : the shape of '+sample_idx+' does not match!')
            print('it has shape of ')
            print(aux.shape)
            print(aux_c0.shape)
            print(aux_c1.shape)
            print(us.shape)
            print(targ.shape)
            allright=False
            thisright=False
        if(thisright):
            for i in range(len(us)):
                for j in range(len(us[0])):
                    for k in range(len(us[0][0])):
                        if(aux[i][j][k]<0):
                            print('warning: the auxlabel of '+sample_idx+' is less than zero, please make sure that it is exactly what you need!')
                            allright=False
                        if(aux_c0[i][j][k]<0 or aux_c0[i][j][k]>10 or aux_c1[i][j][k]<0 or aux_c1[i][j][k]>10):
                            print('fatal error : the feature result from '+sample_idx+' is not between 0-10!')
                            allright=False
                        if(us[i][j][k]<0 or us[i][j][k]>255):
                            print('fatal error : the original image from ' + sample_idx + ' is not between 0-255!')
                            allright = False
                        if(targ[i][j][k].dtype!='uint8'):
                            print('fatal error : the targ from ' + sample_idx + ' is not an integer type, it will surely cause error!')
                            allright = False

                        if(targ[i][j][k]!=0 and targ[i][j][k]!=1):
                            print(
                                'fatal error : the targ from ' + sample_idx + ' is not 1 or 0 , it will surely cause error in a two classification problem!')
                            allright = False

    if(allright):
        print('all the files in data_ini has been checked')
    else:
        print('other files has been checked')



