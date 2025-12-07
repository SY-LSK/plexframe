import argparse
from json import load

from src_py.main_core import create_webview_app,run # type: ignore



cmdparser = argparse.ArgumentParser()

#cmdparser.add_argument('filepath',nargs='?',default='src/main.html',help='文件路径（可选，默认：src/main.html）')
cmdparser.add_argument('--config',nargs='?',default='config.json',help='配置文件路径（可选，默认：config.json）')

args = cmdparser.parse_args()


if args.config:
    with open(args.config, 'r') as f:
        config = load(f)
else:
    config = {}


create_webview_app(config)

if __name__ == '__main__':
    run(config)