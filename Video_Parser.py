import yt_dlp
import os
import re

def create_directory_from_url(video_url):
    """
    Создает директорию на основе URL. 
    

    """
  
    sanitized_url = re.sub(r'[^\w\-_\. ]', '_', video_url)
    
    # Ограничивает длину имени папки
    folder_name = sanitized_url[:50]  # Ограничение до 50 символов
    
    # Создает папку, если её нет
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    return folder_name

def download_videos(video_url, playlist=False):
    """
    Скачивает видео по указанной ссылке с возможностью скачивания плейлистов.
    
    """
    # Создает папку для скачивания
    download_folder = create_directory_from_url(video_url)
    
    ydl_opts = {
        'format': 'best',  
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Сохраняет файл в новую папку
        'noplaylist': not playlist,  # По умолчанию не скачивает плейлист
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', 'Видео без названия')
        print(f"Начинаем скачивание: {video_title}")
        ydl.download([video_url])
        print(f"Загрузка завершена: {video_title}")
        print(f"Видео сохранено в папке: {download_folder}")

def get_playlist_option():
     
    choice = input("Скачать плейлист целиком? (y/n): ").lower()
    return choice == 'y'

def main():
    video_url = input("Введите ссылку на видео или плейлист: ")

    if video_url:
        playlist = get_playlist_option()

        print(f"Скачиваем видео по ссылке: {video_url}")
        download_videos(video_url, playlist)
    else:
        print("Ссылка на видео не введена.")

if __name__ == "__main__":
    main()
