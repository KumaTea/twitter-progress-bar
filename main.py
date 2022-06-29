from image import *
# from time import sleep
from session import kuma
from symlink import symlink
# from sessionWeb import get_driver
# from selenium.webdriver.common.by import By


# def get_followers_count(user):
#     url = f'https://twitter.com/{user}'
#     driver = get_driver()
#     try:
#         driver.get(url)
#         sleep(1)
#         href = f'/{user}/followers'
#         followers_element = driver.find_element(By.XPATH, f'//a[@href=\"{href}\"]')
#         followers_count_text = followers_element.find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'span').text
#         # driver.get('about:blank')
#         driver.quit()
#         return int(followers_count_text.replace(',', ''))
#     except Exception as error:
#         print('    Failed to get followers count using Selenium:')
#         print('      ' + str(error))
#         driver.quit()
#         raise RuntimeError


# def get_followers():
#     return get_followers_count('KumaTea0')


if __name__ == '__main__':
    # Get followers count
    print('  Getting info...')
    # try:
    #     followers = get_followers()
    #     using_selenium = True
    # except:
    me = kuma.get_user(screen_name='KumaTea0')
    followers = me.followers_count
    using_selenium = False
    print('    Followers:', followers)

    # Get last followers count
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
    profile_image = gen_profile_image(progress_image, followers, ppl=ppl, selenium=using_selenium)
    date = now.strftime('%Y%m%d')
    time = now.strftime('%H%M%S')

    print('  Writing image...')
    file_path = f'tmp/{date}{time}.png'
    profile_image.save(file_path)

    print('  Setting new profile image...')
    kuma.update_profile_image(file_path)
    symlink(file_path)
    print('  Done')
