import os
from typing import List


def _createLogger(name, filepath):
    ''' ロガーを作成 '''
    from logging import getLogger, FileHandler, Formatter, DEBUG

    log = getLogger(name)
    log.setLevel(DEBUG)

    fh = FileHandler(filepath, encoding='utf-8')
    fh.setLevel(DEBUG)
    fh_formatter = Formatter(
        '%(asctime)s [%(levelname)s] %(filename)s %(funcName)s():\n%(message)s')
    fh.setFormatter(fh_formatter)

    log.addHandler(fh)
    return log


def _convert_images(target_dir: str) -> List[str]:
    ''' webpに画像を変換 '''
    from glob import glob
    from datetime import datetime, timedelta
    from PIL import Image

    files = glob(f'{target_dir}/**/*', recursive=True)
    ext = ['PNG', 'JPG', 'JPEG']
    cnt = 1
    dt = datetime.utcnow() + timedelta(hours=9)
    t = dt.strftime('%Y-%m-%d_%H-%M-%S')
    for file in files:
        if file[file.rfind('.')+1:].upper() in ext:
            fname = f'{t}_{cnt}'
            dirname: str = os.path.dirname(file)
            img = Image.open(file)
            img.save(f'{dirname}/{fname}.webp')
            cnt += 1

    return glob(f'{target_dir}/**/*.webp', recursive=True)
