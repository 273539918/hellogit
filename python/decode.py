#!/usr/bin/python
# -*- coding: UTF-8 -*-
## unicode编码字符串 解码后输出
#str1 = '\u4f60\u597d'
str1 = '\\u7cfb\\u7edf\\u9519\\u8bef: \\u5185\\u90e8\\u9519\\u8bef, \\u8bf7\\u8054\\u7cfb\\u7cfb\\u7edf\\u7ba1\\u7406\\u5458\\u4fee\\u590d!'
print str1.decode('unicode_escape')