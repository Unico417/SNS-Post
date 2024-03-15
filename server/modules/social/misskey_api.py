from typing import List
from logging import Logger
from misskey import Misskey
from modules.social.socials import APIPlatform


class MisskeyAPI(APIPlatform):

    @classmethod
    def send(
        cls,
        text: str,
        images: List[str] = [],
        account: dict = {},
        log: Logger = None
    ):
        ''' ノートを投稿 '''

        if not account:
            if log:
                log.info('Account invalid.')
                log.info(f'{"Text": > 10}: {text}')
                log.info(f'{"Images": > 10}: {images}')
                log.info(f'{"Social": > 10}: {account}')
            return

        # クラスを作成
        host = account['host']
        api = Misskey(host)
        api.token = account['token']
        if log:
            log.info(f'{"misskey instance": >20}: {"instance"}')
            log.info(f'{"misskey token": >20}: {api.token}')

        # 画像を投稿
        image_ids = cls._post_images(api, images)
        if log:
            log.info(f'{"Image ids": >20}: {image_ids}')

        # ノートを投稿
        api.notes_create(text=text, file_ids=image_ids)
        if log:
            log.info('    ... Done.')

    @classmethod
    def _post_images(cls, api: Misskey, images: List[str] = [], log: Logger = None) -> list[str]:
        ''' 画像を登録 -> str[] 登録されたID'''

        # エラー処理
        if (images is None)\
                or (not ((type(images) is list) or (type(images) is tuple)))\
                or (len(images) == 0):
            return None

        # 画像からidを取得
        ids: List[str] = []
        for image in images:
            with open(image, 'rb') as f:
                data: dict = api.drive_files_create(f)
                id: str = data['id']
                ids.append(id)
        return ids
