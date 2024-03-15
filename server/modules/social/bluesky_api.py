from typing import List, Dict
from logging import Logger
from atproto import Client
from modules.social.socials import APIPlatform


class BlueskyAPI(APIPlatform):

    @classmethod
    def send(
            cls,
            text: str,
            images: List[str] = [],
            account: Dict[str, str] = {},
            log: Logger = None
    ):
        ''' 投稿 ※画像一枚 '''

        # ログイン
        client = Client(account['host'])
        client.login(
            account['serviceID'],
            account['token']
        )

        # TODO:
        if 1 <= len(images):
            images = [images[0]]

        # 画像をロード
        image = None
        for img in images:
            with open(img, 'rb')as f:
                image = f.read()

        # 投稿
        client.send_image(
            text,
            image=image,
            image_alt='',
            langs=['ja'])

        if log:
            log.info('... Done.')
