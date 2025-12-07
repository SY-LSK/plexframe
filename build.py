import argparse
from json import load
from subprocess import run
from os import remove
from sys import exit
#from shutil import rmtree


def get_build() -> dict:
    return config.get('build')

cmdparser = argparse.ArgumentParser()
cmdparser.add_argument('--config', default='config.json')
args = cmdparser.parse_args()

with open(args.config, 'r') as f:
    config = load(f)

cmd = ['pyinstaller','--windowed']

if get_build().get('onefile',False):
    cmd.append('--onefile')

if get_build().get('name','plexframe'):
    cmd.extend(['--name',get_build().get('name','plexframe')])

if get_build().get('icon',False):
    cmd.extend(['--icon',get_build().get('icon')])

if  not config.get('url','').startswith(('http','https')):
    cmd.extend(['--add-data', 'src;src'])

cmd.extend(['--add-data', 'config.json;.',
        '--add-data', 'src_py/fn.py;.',
        '--hidden-import', 'webview',
        '--hidden-import', 'webview.platforms.winforms',
        'src_py/main_core.py'])


print('正在打包应用...')
run(cmd,shell=True)

#rmtree('build',ignore_errors=True)
try:
    remove(f'{config.get('build',{}).get('name', 'plexframe')}.spec')
except:
    pass
exit()