import os, sys
import subprocess
import datetime as dt
import time
import getpass
import json

try:
    subprocess.check_output(['git', '--version'])
except:
    print "git no se encuentra instalado"
    raw_input("")
    sys.exit()
   
def setIdentity():
    subprocess.check_output(['git', 'config', 'user.name', '{0}'.format(getpass.getuser())])
    subprocess.check_output(['git', 'config', 'user.email', '{0}@default.com'.format(getpass.getuser())])

    cred = subprocess.check_output(['cmdkey', '/List']).split('\n')
    if '    Usuario: gdgithub\r' not in cred:
        subprocess.check_output(['cmdkey', '/generic:LegacyGeneric:target=git:https://github.com', '/user:gdgithub', '/pass:ipad3ios6'])

def setRemote():
    try:
        if not subprocess.check_output(['git','remote','-v']):
            remote = subprocess.check_output(['git', 'remote', 'add', 'origin', 'https://github.com/gdgithub/share.git']) 
            print "Se ha agregado el repositorio remoto"
    except:
        pass
   
def pushGitHub():
    diff = subprocess.check_output(['git', 'status'])
    aux = diff.split('\n')
    if "nothing to commit, working tree clean" not in aux:
        date = str(dt.datetime.now())
        os.system('git add .')
        os.system('git commit -m "{0}"'.format(date))
        os.system('git push origin master')
    else:
        print 'No hay cambios'


subprocess.check_output(['git','init'])
setIdentity()
setRemote()

while True:
    subprocess.check_output(['git', 'pull', 'origin', 'master'])
    pushGitHub()
    time.sleep(2)