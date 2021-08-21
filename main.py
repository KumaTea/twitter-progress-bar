from image import *
from session import kuma


if __name__ == '__main__':
    print('  Getting info...')
    me = kuma.me()
    followers = me.followers_count
    print('    Followers:', followers)
    ppl = int(str(followers)[-2:])
    try:
        with open('foer.txt', 'r') as f:
            old_foer = f.read()
    except:
        old_foer = 0
    if int(old_foer) == followers:
        print('  No changes!')
        exit(0)
    else:
        with open('foer.txt', 'w') as f:
            f.write(str(followers))

    print('  Generating image...')
    progress_image = gen_progress_image(ppl)
    profile_image = gen_profile_image(progress_image, followers, ppl=ppl)
    date = now.strftime('%Y%m%d')
    time = now.strftime('%H%M%S')

    print('  Writing image...')
    file_path = f'tmp/{date}{time}.png'
    profile_image.save(file_path)

    print('  Setting new profile image...')
    kuma.update_profile_image(file_path)
    print('  Done')
