from logging import Logger
from typing import List
import tweepy
from modules.social.socials import APIPlatform


class TwitterAPI(APIPlatform):

    @classmethod
    def send(
        cls,
        text: str,
        images: List[str] = [],
        account: dict = {},
        log: Logger = None
    ) -> None:
        ''' Twitterに投稿 '''

        # API v1 - 画像投稿
        auth = tweepy.OAuthHandler(
            account['apiKey'],
            account['apiKeySecret'],
        )
        auth.set_access_token(
            account['accessToken'],
            account['accessSecret'],
        )
        api = tweepy.API(auth)

        # API v2
        client = tweepy.Client(
            consumer_key=account['apiKey'],
            consumer_secret=account['apiKeySecret'],
            access_token=account['accessToken'],
            access_token_secret=account['accessSecret'],
        )

        # 画像アップロード
        media_ids = []
        for image in images:
            media = api.media_upload(filename=image)
            media_ids.append(media.media_id)

        # ツイート
        client.create_tweet(text=text, media_ids=media_ids)
