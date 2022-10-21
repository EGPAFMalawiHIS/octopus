#!/usr/bin/env python3

import os
import subprocess
import sys
import os.path
import typer


'''
Installing application dependencies
'''

package_list = [
   'sudo apt-get update',
   'sudo apt-get -y install python3-pip',
   'sudo apt install python3-django'
]

for package in package_list:
   print("____________________________________________________________________________________________")
   print(package)
   print("............................................................................................")
   _process = subprocess.run(package.split(), stdout=subprocess.PIPE)
   print(_process.stdout)

   if _process.returncode != 0:
      print(_process.stderr)

def run(cmd, die_on_fail=True):
    print('Running: {cmd}..............................'.format(cmd=cmd))
    if os.system(cmd) == 0:
        return True

    sys.stderr.write('error: Operation failed: {cmd}\n'.format(cmd=cmd))
    if die_on_fail:
        exit(255)    

    return False

'''
create a virtual environment for the app
Install requirements package
Run migrations
'''
  
run("python3 -m venv env")
run(". env/bin/activate")

_process=subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements/local.txt"])
print("Running migrations........................................................................")
run("python3 manage.py migrate")

print("..........................................................................................")
print("Installation completed successfully!!! You can now start your application in development by typing the command: [python3 manage.py runserver]")
      
   
