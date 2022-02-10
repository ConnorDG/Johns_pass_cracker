from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from animal_name_list import animal_ary


def start_login():
    website = "https://erau.instructure.com/courses/138212/quizzes/461341/take?user_id=321998"
    web = webdriver.Chrome()
    web.get(website)
    user_box = web.find_element(By.XPATH, '//*[@id="username"]')
    user_box.send_keys("coffeej5")
    pass_box = web.find_element(By.XPATH, '//*[@id="inputPassword"]')
    # pass_box.send_keys("Raccoon4life212", Keys.RETURN)
    pass_box.send_keys("Raccoon4life212")


def try_pass(password):
    box = web.find_element_by_xpath('password')
    box.send_keys(password)
    submit = web.find_element_by_id('login-form-submit')
    submit.click()


if __name__ == "__main__":
    start_login()

"""
for name in animal_ary:
    print(name)
    try_pass(name)
    time.sleep(1)
"""
