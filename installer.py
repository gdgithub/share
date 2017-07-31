import os, sys
import subprocess
import urllib2

downloadPath = os.path.expandvars('%tmp%')
url = "https://github.com/git-for-windows/git/releases/download/v2.13.3.windows.1/Git-2.13.3-32-bit.exe"
filename = url.split('/')[-1]

def downloadFile(url, dest=os.path.expandvars('%tmp%')):
    u = urllib2.urlopen(url)

    with open(dest+'\\{0}'.format(filename), 'wb') as f:
        meta = u.info()
        metalength = meta.getheaders('Content-Length')[0]
        filesize = None
        if metalength:
            filesize = int(metalength)
        print("Descargando {0}, Bytes: {1}".format(filename, filesize))

        file_size_dl = 0
        blocks = 8192

        while True:
            buffer = u.read(blocks)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
    
            status = ""
            if filesize:
                status += "{0:6.2f}%".format(file_size_dl*100.0/filesize)
            status += chr(13)

            print(status)
        return filename

if not os.path.exists(downloadPath+'\\git.inf'):
    downloadFile(url)

gitInf = """[Setup]
Lang=default
Dir=C:\Program Files (x86)\Git
Group=Git
NoIcons=0
SetupType=default
Components=ext,ext\shellhere,ext\guihere,gitlfs,assoc,assoc_sh
Tasks=
"""

with open(downloadPath+'\\git.inf', 'w') as f:
    f.write(gitInf)

print "Se procedera a instalar Git"
subprocess.check_output([downloadPath+'\\'+filename, '/LOADINF="git.inf"', '/SILENT',])
