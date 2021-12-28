from session import kuma
from selenium import webdriver as wd


options = wd.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--user-data-dir=/home/kuma/data/chrome')
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-software-rasterizer")


def get_driver():
    return wd.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
