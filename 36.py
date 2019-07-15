import re

def is_valid_email(addr):
       jc = re.compile(r'~\w+.*\w+@\w+.\w+$')
       if re.match(jc,addr):
              return True
       
