"""
输出重定向
默认情况下，print 函数会将内容打印输出到标准输出流(即 sys.stdout)，可以通过 file 参数自定义输出流。

也可以输出到错误输出流，例如：
"""

with open('data.log', 'w') as fileObj:
    print('hello world!', file=fileObj)

import sys

print('hello world!', file=sys.stderr)