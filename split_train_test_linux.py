#!/usr/bin/env python
# -*- coding UTF-8 -*-
# File: split_train_test.py

import os
import shutil
#import numpy as np

def split_train_test(data_dir):
    split_dir = 'ucfTrainTestlist'
    origin_dir = 'UCF-101'
    
    os.mkdir(os.getcwd()+'/train')
    for i in range(3):
        with open(split_dir+'/trainlist0'+str(i+1)+'.txt') as f:
            train_list = f.readline()
            train_list = train_list[:train_list.find('.avi')+4]
            if not os.path.exists(os.getcwd()+'/train/'+train_list.split('/')[0]):
                os.mkdir(os.getcwd()+'/train/'+train_list.split('/')[0])
            shutil.copy(os.getcwd()+'/'+origin_dir+'/'+train_list,\
                        os.getcwd()+'/train/'+train_list)
            
            while train_list:
                train_list = f.readline()
                if train_list == '':
                    break
                train_list = train_list[:train_list.find('.avi')+4]
                if not os.path.exists(os.getcwd()+'/train/'+train_list.split('/')[0]):
                    os.mkdir(os.getcwd()+'/train/'+train_list.split('/')[0])
                shutil.copy(os.getcwd()+'/'+origin_dir+'/'+train_list,\
                            os.getcwd()+'/train/'+train_list)
    
    
    os.mkdir(os.getcwd()+'/test')
    for i in range(3):
        with open(split_dir+'/testlist0'+str(i+1)+'.txt') as f:
            test_list = f.readline()
            test_list = test_list[:-1]
            if not os.path.exists(os.getcwd()+'/test/'+test_list.split('/')[0]):
                os.mkdir(os.getcwd()+'/test/'+test_list.split('/')[0])
            shutil.copy(os.getcwd()+'/'+origin_dir+'/'+test_list,\
                        os.getcwd()+'/train/'+test_list)
            
            while test_list:
                test_list = f.readline()
                if test_list == '':
                    break
                test_list = test_list[:-1]
                if not os.path.exists(os.getcwd()+'/test/'+test_list.split('/')[0]):
                    os.mkdir(os.getcwd()+'/test/'+test_list.split('/')[0])
                shutil.copy(os.getcwd()+'/'+origin_dir+'/'+test_list,\
                            os.getcwd()+'/test/'+test_list)
    
        

if __name__ == '__main__':
    data_dir = os.getcwd() #UCF的上一级目录
    split_train_test(data_dir)

