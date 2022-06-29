from selenium import webdriver as wd


options = wd.FirefoxOptions()
options.headless = True
# options.add_argument('--headless')
# options.add_argument('--user-data-dir=/home/kuma/data/chrome')
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-software-rasterizer")


def get_driver():
    driver = wd.Firefox(options=options)
    return driver
