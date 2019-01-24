import subprocess
import os
import urllib.request
import urllib.parse
from urllib.request import urlopen as p

#with urllib.request.urlopen('http://python.org/') as response:
    #html = response.read()
    #print("response-",html)
url = 'https://www.google.com/search?q=python'

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
respData = resp.read()
saveFile = open('withHeaders.txt','w')
saveFile.write(str(respData))
saveFile.close()


########for shell command execution in python and return exit status only
#cmd = 'wc -l my_text_file.txt > out_file.txt'
#os.system(cmdVar1)


########for shell command execution and retun out put

def shellCommand(cmdVar):
    out = subprocess.Popen("cmdVar", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    (output, err) = out.communicate()
    p_status = out.wait()
    return output

cmdOut = shellCommand("dir")
#print("OUTPUT----------",cmdOut)