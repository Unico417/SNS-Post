from typing import List


def send(
    text: str,
    tempdir: str,
    images: List[str] = [],
    config: dict = {},
    account_keys: List[str] = [],
) -> None:
    ''' temp ディレクトリの画像を送信する '''
    from modules.social.utils import _createLogger
    from modules.social.socials import send_all

    if (not account_keys) \
            or ((not text) and (not images)):
        return

    # ロガー作成
    log = _createLogger('SOCIAL', f'{tempdir}/log.log')

    accounts = []
    for key in account_keys:
        accounts.append(config['accounts'][key])

    log.info(f'{"Text": >10}: {text}')
    log.info(f'{"Images": >10}: {images}')
    log.info(f'{"Accounts": >10}: {accounts}')

    # 今のところ画像は一枚のみ
    # 上限3MB
    send_all(
        text,
        images=images,
        accounts=accounts,
        log=log
    )
