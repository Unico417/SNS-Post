import os
import json
from glob import glob

from flask import Flask, request
from flask_cors import CORS

from modules.social import send
from modules.social.utils import _convert_images

rootdir = os.path.abspath(os.path.dirname(__file__))
tempdir = f'{rootdir}/temp'

api = Flask(__name__)
CORS(api)

config = {}
with open(f'{tempdir}/config.json', mode='r', encoding='utf-8') as f:
    config = json.load(f)


@api.route('/post', methods=['POST'])
def post():

    # ファイルの取得
    file = request.files['image']
    text = request.form['text']

    # ファイルの変換
    file.save(os.path.join(tempdir, file.filename))
    images = _convert_images(tempdir)
    images = glob(f'{tempdir}/**/*.webp', recursive=True)

    # 送信
    try:
        send(
            text,
            tempdir,
            account_keys=config['accounts'].keys(),
            config=config,
            images=images,
        )
    except:
        import traceback
        traceback.print_exc()

    # ファイル削除
    ext = ('png', 'jpg', 'jpeg', 'webp')
    image_files = [
        file for file in glob(os.path.join(tempdir, '*'))
        if file.lower().endswith(ext)
    ]

    for image_file in image_files:
        try:
            os.remove(image_file)
        except Exception:
            pass

    return 'done'


if __name__ == '__main__':
    import webbrowser

    # ブラウザを開く
    htmlpath = os.path.abspath(f'{rootdir}/../public/index.html')
    webbrowser.open_new_tab(f'file:///{htmlpath}')

    # apiサーバーを開く
    api.run(host='127.0.0.1', port=config['path'])
