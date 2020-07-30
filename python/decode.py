#!/usr/bin/python
# -*- coding: UTF-8 -*-
## unicode编码字符串 解码后输出
#str1 = '\u4f60\u597d'
str1 = '\\u64cd\\u4f5c\\u9519\\u8bef: \\u533a\\u57df\\u540d\\u79f0\\u4e0d\\u80fd\\u5b58\\u5728\\uff0c\\u8bf7\\u4fee\\u6539\\u533a\\u57df\\u540d\\u79f0\\u540e\\u5c1d\\u8bd5\\u91cd\\u65b0\\u63d0\\u4ea4\\u3002'
print str1.decode('unicode_escape')