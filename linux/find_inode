#!/bin/bash

## 遍历目录，输出inode大小
echo "执行的文件名: $0"
echo "第一个参数为: $1"
for i in $1/*
do
    echo $i
    sudo find $i | wc -l
done