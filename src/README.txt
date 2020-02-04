训练相关：所有数据位于\train文件夹

us文件夹为原始图，命名为0.mat,1.mat,....每个.mat为一个3D的数据。默认进行除以255的归一化。


targ文件夹是groundtruth(groundtruth文件夹不是aux_label文件夹!)，每个元素必须为整型0或1，否则将会进行强制类型转换，产生意想不到的后果。每个3D图像依次命名为0_seg.mat,1_seg.mat,2_seg.mat...  ，和ｕｓ对应。

aux_map文件夹为stage1的概率图，每个元素默认为0-1之间的数，不进行额外归一化。对于每张图，例如0.mat,其血管和背景的概率图分别命名为0_aux_0.mat和0_aux_1.mat。例如140.mat,其两个概率图命名为140_aux_0.mat和140_aux_1.mat。

aux_label不是groundtruth，而是第一阶段网络的结果的label，之所以需要这一项是由于网络的boundingbox聚焦机制，如果不需要学习某部分，直接在一阶段将其aux_label标记为某个负数即可。网络将会考虑边缘地将大于等于0的label对应的部分喂进网络学习。如果一阶段label只有0和1，boundingbox机制自动无效。


网络参数可以从..\outcome\model\ini\下的ini文件修改，其中值得注意的是img_n是一共的图片数量(也即us文件夹中的原始图数量)，其余参数均是网络本身的特性的参数，不再赘述。
训练后的网络位于..\outcome\model。与此同时，每完成三次训练(epoch)，保存一次参数。

测试相关：所有数据位于\test文件夹中，命名方式和训练数据集的命名相同。每个3D.mat文件生成的结果保存在segment_result中，已经是label（整型0，1）

关于theano的GPU环境配置，参考GPU配置.txt











