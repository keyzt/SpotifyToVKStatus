# Spotify To VK Status
**Spotify To VK Status** - модуль для трянсляции прослушиваемых треков из Spotify в статуст ВКонтакте.

# Установка
1. Склонируйте репозиторий (или просто скачайте [его](https://github.com/keyzt/SpotifyTo-VK-Status/archive/master.zip)) и перейдите в директорию с проектом.
```bash
git clone https://github.com/keyzt/spotifyTo-VK-Status.git #
cd spotifyTo-VK-Status
```
2. Установите необходиме зависимости:
	- Используя **Poetry**: ```poetry install --no-dev```
	- Используя pip: ```pip install -r requirements.txt```
3. Создайте в корне директории проекта файл конфигурации `.env`, и настройте его согласно `env.example`.
	- Создайте свое приложение [тут](https://developer.spotify.com/dashboard/applications).
	- Заполните поля в конфиге согласно вашим значениям.

# Использование

Обычный запуск:
```
python -m app
```

Запуск при помощи **Poetry**:
```
poetry run python -m app
```
