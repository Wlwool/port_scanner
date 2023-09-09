# from pytube import YouTube
#
# # Укажите URL-адрес видео на YouTube
# video_url = "https://www.youtube.com/watch?v=XiKl3sa29uo"
#
# # Создайте объект YouTube
# yt = YouTube(video_url)
#
# # Выбирает поток с самым высоким разрешением
#
# stream = yt.streams.get_highest_resolution()
# # выходной путь для загруженного видео
# output_path = "/home/dima/PycharmProjects/py_tst/sttest/muz"
#
# # Загрузка видео
# stream.download(output_path)
#
# print("Видео успешно загружено!")

# Код ниже работает

from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Загрузка выполнена успешно")


link = input("Enter the YouTube video URL: ")
Download(link)
