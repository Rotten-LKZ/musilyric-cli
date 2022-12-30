# folder_path = input('Welcome to use Musilyric-cli\nInput absolute folder path where music files are\nInput: ')
# print(f'Folder path: {folder_path}')

# overwrite = input('Do you wanna overwrite your existing lyric tag?\nInput([Y]es, [N]o): ')
# if overwrite.lower() == 'yes' or overwrite.lower() == 'y':
#     overwrite = True
# else:
#     overwrite = False
# print(f'You chose {" " if overwrite else "not "}to overwrite.')

import os
import mutagen

dirs = []


def get_all_files(path):
    global dirs
    _files = []
    dirs = os.listdir(path)
    for _dir in dirs:
        if not os.path.isdir(_dir):
            if _dir.endswith('.mp3') or _dir.endswith('.flac') or _dir.endswith('.ogg'):
                _files.append(_dir)

    return _files


def find_lyric(name):
    global dirs
    for _dir in dirs:
        if not os.path.isdir(_dir):
            if (_dir.endswith('.txt') or _dir.endswith('.lrc')) \
                    and (_dir == f'{name}.txt' or _dir == f'{name}.lrc' or _dir.split('.')[0] == name.split('.')[0]):
                return _dir

    return None


if __name__ == '__main__':
    folder_path = r'D:\Music\自下\test_collection'
    overwrite = True

    dirs = os.listdir(folder_path)

    files = get_all_files(folder_path)
    success_files = []

    for file in files:
        mutagen_file = mutagen.File(os.path.join(folder_path, file))
        if mutagen_file.get('lyrics') is not None and overwrite is False:
            continue

        lyric_res = find_lyric(file)

        if lyric_res is not None:
            f = open(os.path.join(folder_path, lyric_res), encoding='utf-8')
            if file.endswith('.flac') or file.endswith('.ogg'):
                mutagen_file['LYRICS'] = [f.read().replace('\n', '\r\n')]
                mutagen_file.save()
                f.close()
            else:
                ...
