import pickle
from selenium.webdriver.common.by import By
import pprint
import time

from selenium import webdriver


def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):#Checks if the instance expiry a float 
            cookie['expiry'] = int(cookie['expiry'])# it converts expiry cookie to a int 
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()


# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "D:\python\python_scraping\cookie.txt"

# Initial load of the domain that we want to save cookies for
chrome = webdriver.Chrome()
chrome.get("https://www.google.com")
chrome.find_element(By.CLASS_NAME, "gb_Hd").click()
chrome.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("9gag.lool.@gmail.com")
chrome.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
time.sleep(5)
chrome.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys("bokep123!")
chrome.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
save_cookies(chrome, cookies_location)
chrome.quit()

# Load of the page you cant access without cookies, this one will fail
# chrome = webdriver.Chrome()
# chrome.get("https://play.google.com/store/apps/details?id=com.app.cumobileonline&pli=1")


# # Load of the page you cant access without cookies, this one will go through
# chrome = webdriver.Chrome()
# load_cookies(chrome, cookies_location)
# chrome.get("https://play.google.com/store/apps/details?id=com.app.cumobileonline&pli=1")

# chrome = webdriver.Chrome()
# chrome.get("https://google.com")
# time.sleep(2)
# pprint.pprint(chrome.get_cookies())
# print ("=========================\n")

# delete_cookies(chrome, domains=["www.google.com"])
# pprint.pprint(chrome.get_cookies())
# print ("=========================\n")

# delete_cookies(chrome)
# pprint.pprint(chrome.get_cookies())