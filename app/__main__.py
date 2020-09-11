import time
import typing
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from VKLight import ( VKLight, VKLightError )
from .config import ( VKConfig, SpotifyConfig )


spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SpotifyConfig.SCOPE,
        client_id=SpotifyConfig.CLIENT_ID,
        client_secret=SpotifyConfig.CLIENT_SECRET,
        redirect_uri=SpotifyConfig.REDIRECT_URI,
        username=SpotifyConfig.USERNAME,
    )
)

vk = VKLight(dict(
        access_token=VKConfig.VK_TOKEN,
        lang='ru',
        host="api.vk.me",
        v='5.130'
    )
)


current_playing = typing.List[typing.Union[str, str, str]]


def update_status(_current_playing):
    current = spotify.current_user_playing_track()

    if not current is None:

        track = current["item"]["name"]
        album = current["item"]["album"]["name"]
        artist = current["item"]["artists"][0]["name"]

        if _current_playing != [track, album, artist]:
            set_status(VKConfig.STATUS.format(track=track, album=album, artist=artist))
            time_now = time.strftime("%H:%M:%S", time.localtime())
            print(f"[{time_now}] 🎧 Spotify | {track} - {artist}")

        return [track, album, artist]

    if not _current_playing is None:
        set_standart_status()
    
    return 


def set_standart_status() -> None:
    print("Установлен стандартный статус")
    return vk.call("status.set", { "text": VKConfig.STANDART_STATUS })


def set_status(status) -> None:
    return vk.call("status.set", { "text": status })


if __name__ == '__main__':
    try:
        VKConfig.STANDART_STATUS = vk("status.get")['response']['text']
        print(f"Текущий статус: {VKConfig.STANDART_STATUS}")

        while True:
            # print("Получаю обновления")
            current_playing = update_status(current_playing)
            time.sleep(8)


    except VKLightError as e:
        print(e)

    except (SystemExit, KeyboardInterrupt) as e:
        set_standart_status()

    except Exception as e:
        print(e)