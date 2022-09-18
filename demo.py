import os
'''
遍历目录树
'''
for folder_name,sub_folders,filenames in os.walk('/'):
    print('当前文件夹：'+folder_name)
    # for sub_folder in sub_folders:
    #     print('所包含的子文件夹：'+sub_folder)
    #     for filename in filenames:
    #         print('文件夹 %s 中所包含的文件：%s' %(folder_name,filename))
    print('')