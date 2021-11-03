from image import *
from time import sleep
from symlink import symlink
from sessionWeb import kuma, driver


def get_followers_count(user):
    url = f'https://twitter.com/{user}'
    driver.get(url)
    sleep(1)
    href = f'/{user}/followers'
    followers_element = driver.find_element_by_xpath(f'//a[@href=\"{href}\"]')
    followers_count_text = followers_element.find_element_by_tag_name('span').find_element_by_tag_name('span').text
    driver.get('about:blank')
    return int(followers_count_text.replace(',', ''))


def get_followers():
    return get_followers_count('KumaTea0')


if __name__ == '__main__':
    print('  Getting info...')
    try:
        followers = get_followers()
    except:
        print('    Failed to get followers count using Selenium.')
        try:
            me = kuma.me()
        except AttributeError:  # tweepy v4
            me = kuma.get_user(screen_name='KumaTea0')
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
    symlink(file_path)
    print('  Done')
