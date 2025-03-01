from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


putBrowser = input("Please enter the number to choose your browser (1 Chrome, 2 Safari, 3 Firefox, 4 Edge): ")
putUsername = input("Type your Roblox Account username here: ")
putPassword = input("Type Roblox Account Password here: ")


match putBrowser:
    case "1":
        print("Ok. Starting Chrome... ")
        browser = webdriver.Chrome()
    case "2":
        print("Ok. Starting Safari... ")
        browser = webdriver.Safari()
    case "3":
        print("Ok. Starting Firefox... ")
        browser = webdriver.Firefox()
    case "4":
        print("Ok. Starting Edge... ")
        browser = webdriver.Edge()
    case _:
        print("Unknown browser!")
        exit()


print("Logging in... ")
browser.get("https://roblox.com/login")


WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
username = browser.find_element(By.ID, "login-username")
password = browser.find_element(By.ID, "login-password")


username.send_keys(putUsername)
password.send_keys(putPassword)


loginBtn = browser.find_element(By.ID, "login-button")
loginBtn.click()


time.sleep(10)


while True:

    idRandom = "626866146"
    print("Following user with ID:", idRandom)

    browser.get(f"https://roblox.com/users/{idRandom}")

    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, "popover-link"))
        )
        userOptions = browser.find_element(By.ID, "popover-link")
        userOptions.click()
        time.sleep(2)

        followUser = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@role='menuitem' and @tabindex='-1' and contains(@href, '#')]"))
        )


        followUser.click()
        print("FOLLOWED! Moving to next random ID...")

    except Exception as e:
        print("Could not follow user with ID:", idRandom, "Error:", e)

    time.sleep(3)
