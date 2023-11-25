import pytube
import os

def download_video(url, file_format, output_path):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=output_path, filename=f'video.{file_format}')
        print('Pobieranie zakończone!')
        
        # Get the file location
        file_location = os.path.join(output_path, f'video.{file_format}')
        
        # Open the file location in the explorer
        os.startfile(file_location)
        
    except Exception as e:
        print(f'Error: {str(e)}')

def welcome_message():
    print('Witaj w programie do pobierania filmów z YouTube!')
    print('Program pobiera film w najwyższej dostępnej jakości.')
    print('Zrobione przez: naroors')
    print('')
    print('')

def main():
    welcome_message()
    url = input('Wklej link do filmu: ')
    file_format = input('Wybierz format pliku (mp3/mp4):')
    output_path = input('Podaj ścieżkę do zapisu pliku:')

    if file_format not in ['mp3', 'mp4']:
        print('Nieprawidłowy format pliku!')
        return

    download_video(url, file_format, output_path)

if __name__ == '__main__':
    main()
