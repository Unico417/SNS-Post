from typing import List, Dict
from logging import Logger


def send_all(
    text,
    images: List[str] = [],
    accounts: List[dict] = [],
    log: Logger = None
):
    from modules.social.bluesky_api import BlueskyAPI
    from modules.social.misskey_api import MisskeyAPI
    from modules.social.twitter_api import TwitterAPI

    SOCIALS: Dict[str, APIPlatform] = {
        'misskey': MisskeyAPI,
        'bluesky': BlueskyAPI,
        'twitter': TwitterAPI,
    }

    for account in accounts:
        platform = account['platform']
        social = SOCIALS[platform]
        social.send(
            text,
            images=images,
            account=account,
            log=log
        )


class APIPlatform:

    @classmethod
    def send(
        cls,
        text,
        images: List[str] = [],
        account: dict = [],
        log: Logger = None
    ):
        if log:
            log.info('Social not found.')
            log.info(f'{"Text": >10}: {text}')
            log.info(f'{"Images": >10}: {images}')
            log.info(f'{"Social": >10}: {account}')
