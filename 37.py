#--coding:utf-8 --

import base64

def seaf_base64(s):
       if len(s) % 4 == 0:
              return base64.b64encode(s)
       else 
