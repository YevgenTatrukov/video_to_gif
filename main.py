import wget
from moviepy.editor import *


def download_video(url='', video_file=''):
    print('-' * 25)
    print('Loading in progress')
    if not os.path.exists('Video'):
        os.mkdir('Video')
    try:
        wget.download(url=url, out=f'video/{video_file}.mp4')
        return 'Video successfully loading'
    except Exception as ex:
        return 'Check the URL address please!'


def convert_video_to_gif(file_name=''):
    gif_file = (VideoFileClip(f'Video/{file_name}.mp4'))
    if not os.path.exists('GIF'):
        os.mkdir('GIF')
    gif_file.write_gif(f'GIF/{file_name}.gif')
    return "Okay I'm finish. Good day! "


def main():
    url_link = input('Input url address video: ')
    video_name = input('Input the name of the saved video: ')
    print(download_video(url=url_link, video_file=video_name))
    print('-' * 25)
    print()
    print('+' * 25)
    print("I'm converting now.")
    print(convert_video_to_gif(file_name=video_name))
    print('+' * 25)


if __name__ == '__main__':
    main()
