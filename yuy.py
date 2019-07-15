# -*- coding: utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyttsx
engine = pyttsx.init()
engine.say('你好')
engine.runAndWait()
# 朗读一次
engine.endLoop()