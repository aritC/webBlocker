import time
from datetime import datetime as dt


import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    print ("I am root now.")

path = "C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'

sites = ["www.facebook.com"]

while(True):

    if dt(dt.now().year , dt.now().month , dt.now().day , 13) < dt.now() < dt(dt.now().year , dt.now().month , dt.now().day , 16):
        print(1)
        with open(path,'r+') as file:
            content = file.read()
            for site in sites:
                if site in  content:
                    pass
                else:
                    file.write("\n"+redirect+" "+site)
    else:
        with open(path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any( site in line for site in sites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
