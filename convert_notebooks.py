import scandir
import os
import re
import subprocess
import pipes

notebook = re.compile('.*\.ipynb$')

targets = []
for subdir, dirs, files in scandir.walk('.'):
    for the_file in files:
        full_name = "{}/{}".format(subdir, the_file)
        try:
            if notebook.match(full_name) and not ('.ipynb_checkpoints' in full_name):
                targets.append(os.path.abspath(full_name))
        except FileNotFoundError:
            pass

plotdir = './html_notebooks'
if not os.path.exists(plotdir):
    os.makedirs(plotdir)
try:
    os.chdir(plotdir)
    for target in targets:
        escaped=pipes.quote(target)
        command='ipython nbconvert --to html {}'.format(escaped)
        status,output=subprocess.getstatusoutput(command)
        print(target,status,output)
except Exception as err:
    print('trouble: {}'.format(err))
finally:
    os.chdir('..')


plotdir = './transfer_notebooks'
if not os.path.exists(plotdir):
    os.makedirs(plotdir)
try:
    os.chdir(plotdir)
    for target in targets:
        escaped=pipes.quote(target)
        command='cp -af {} .'.format(escaped)
        status,output=subprocess.getstatusoutput(command)
        print(target,status,output)
except Exception as err:
    print('trouble: {}'.format(err))
finally:
    os.chdir('..')
    

plotdir = './pdf_notebooks'
if not os.path.exists(plotdir):
    os.makedirs(plotdir)
try:
    os.chdir(plotdir)
    for target in targets:
        escaped=pipes.quote(target)
        command='ipython nbconvert --to latex {}'.format(escaped)
        status,output=subprocess.getstatusoutput(command)
        print(target,status,output)
except Exception as err:
    print('trouble: {}'.format(err))
finally:
    os.chdir('..')
    
