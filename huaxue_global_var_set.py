#copy from http://t.zoukankan.com/wulixia-p-14942434.html


#调用方法
#import huaxue_global_var_set
#import huaxue_global_var_cofig as glv
# ...
#glv.get_var("变量名")
#估计可以删除"_"（下划线）

import huaxue_global_var_cofig as glv

glv.var_init()
#以下填变量配置

#全局字体
glv.set_var("font_set", "./font/fz.ttf")
#碰一棵树扣几分
glv.set_var("deduct_score", "10")
#碰一个金币加几分
glv.set_var("add_score", "10")
#初始分数
glv.set_var("initial_score", "500")
#over分数(要大于初始分数)
glv.set_var("over_score", "10")
