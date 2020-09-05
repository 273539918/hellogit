#!/usr/bin/python
# -*- coding: UTF-8 -*-
## unicode编码字符串 解码后输出
#str1 = '\u4f60\u597d'
str1 = '\\u64cd\\u4f5c\\u9519\\u8bef: \\u9879\\u76ee\\u540d\\u79f0\\u5df2\\u7ecf\\u5b58\\u5728\\uff0c\\u9879\\u76ee\\u540d\\u79f0\\u4e0d\\u5141\\u8bb8\\u91cd\\u540d\\uff0c\\u8bf7\\u4fee\\u6539\\u60a8\\u7684\\u9879\\u76ee\\u540d\\u3002'
print str1.decode('unicode_escape')