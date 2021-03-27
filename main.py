#!/usr/bin/python3
#-*- encoding:utf-8 -*-
import os
import sys
from optparse import OptionParser
from optparse import IndentedHelpFormatter
#from pyfiglet import Figlet
import pickle


#print(Figlet(font='slant').renderText('HeyTranser'))
"""
    __  __          ______
   / / / /__  __  _/_  __/________ _____  ________  _____
  / /_/ / _ \/ / / // / / ___/ __ `/ __ \/ ___/ _ \/ ___/
 / __  /  __/ /_/ // / / /  / /_/ / / / (__  )  __/ /
/_/ /_/\___/\__, //_/ /_/   \__,_/_/ /_/____/\___/_/
           /____/
"""
print(__doc__)
class NoWrapFormatter(IndentedHelpFormatter) :
    def _format_text(self, text) :
        "[Does not] format a text, return the text as it is."
        return text

parser = OptionParser(prog='HeyTranser Writer',
                              usage="",
                              description="HeyTranser Writer",
                              version="1.0",
                              formatter=NoWrapFormatter(),
                              epilog="""Thanks for using!
                              """)

#源语言,程序语言/自定义语言规则,是否首次,是否已注释方式将翻译信息保存至文件,完整/直接trs函数,

#是否手动引入SDK,是否完整回显,
#日志级别

parser.add_option("-p", "--projectdir",
                 dest="Dir",
                help="工程根目录")                
parser.add_option("-t", "--htproject",
                 dest="Dir",
                help="HT工程")       
parser.add_option("-s", "--first",
                 dest="T/F", default='True',
                help="是否首次")
parser.add_option("-a", "--issave",
                 dest="T/F", default="False",
                help="是否以注释方式将翻译信息保存至文件")                
parser.add_option("-f", "--isfullfunc",
                 dest="T/F", default='False',
                help="完整/直接trs函数")
parser.add_option("-d", "--isautosdk",
                 dest="T/F",
                help="是否手动引入SDK")
parser.add_option("-b", "--isfullback",
                 dest="T/F",
                help="是否完整回显")
parser.add_option("-g", "--loglevel",
                 dest="Level",
                help="日志级别")     
type(parser.parse_args())                       
(options, args) = parser.parse_args()

values=options.__dict__
def CheckValue(values):
    """
    values
    """
    if values['']=='' :
        pass
    else:
        pass