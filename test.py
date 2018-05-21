#!/usr/bin/env python3

import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from util.cli_helper import get_all_user_names
import util.extractor

from pprint import pprint

chrome_options = Options()

browser = webdriver.Chrome('./drivers/chromedriver', chrome_options=chrome_options)

browser.get("https://photos.app.goo.gl/id10fyq9DCIpxMQX2")

images = browser.find_elements_by_class_name("rtIMgb")

test_image = images[0]
test_image.click()
image = browser.find_elements_by_class_name("rtIMgb")
pprint(image)

# for image in images:
#     image.click()
#     image = browser.find_elements_by_class_name("rtIMgb")
#     pprint(image)


images[0].get_screenshot_as_file("testing.png")
pprint(images)


driver.close()