# -*- coding: utf-8 -*-
# Author: 小狼狗
import pkuseg
import torch
# seg = pkuseg.PKUSeg()                                  # 以默认配置加载模型
# text = seg.cut('我爱北京天安门')                        # 进行分词
# print(text)
#
# a = torch.randn(4, 4)
# b = torch.randn(4,4)
# print(a)
# print(b)
# MIN = torch.min(a,b)
# print(MIN)
#
# loss = torch.log(1.0 + torch.exp(torch.Tensor([1.0,2.0])))
# print(loss)

i = 0
for j in range(7):
    x = j + i
    print(x)
    i = i + 1