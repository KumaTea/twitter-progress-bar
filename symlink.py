import os


home = '/home/kuma'
this_proj = 'tt/twitter-progress-bar'
link = 'www/s/prog/avatar.png'


def symlink(file):
    target = f'{home}/{this_proj}/{file}'
    os.remove(f'{home}/{link}')
    return os.system(f'ln -s {target} {home}/{link}')
