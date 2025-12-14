# =============================================
# PROJECT: Selenium Automation – Auto Login & Report Download
# AUTHOR: Santhosh Kumar (santhoshk-dev)
# USE CASE: Freelancing / Business Automation
# =============================================

"""
PROJECT OVERVIEW
----------------
This Selenium automation script:
✔ Opens a website
✔ Logs in automatically
✔ Navigates to a page
✔ Takes screenshot / downloads report

This is a HIGH-DEMAND freelancing project.
Clients use this for portals, admin panels, dashboards.

NOTE:
This demo uses a sample login site.
You can adapt selectors for any real client website.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# ---------------- CONFIG ----------------
LOGIN_URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"      # demo username
PASSWORD = "SuperSecretPassword!"  # demo password

SCREENSHOT_FOLDER = "screenshots"
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

# ---------------- SETUP DRIVER ----------------
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

# ---------------- LOGIN FUNCTION ----------------
def login(driver):
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)

    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    print("[+] Login submitted")

# ---------------- AFTER LOGIN TASK ----------------
def post_login_task(driver):
    wait = WebDriverWait(driver, 10)

    success_message = wait.until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    print("[+] Login response:", success_message.text)

    # Take screenshot
    screenshot_path = os.path.join(SCREENSHOT_FOLDER, "login_success.png")
    driver.save_screenshot(screenshot_path)
    print(f"[+] Screenshot saved: {screenshot_path}")

# ---------------- MAIN ----------------
def main():
    driver = setup_driver()

    try:
        login(driver)
        time.sleep(10)
        post_login_task(driver)
        time.sleep(10)
        print("[✓] Automation completed successfully")
    except Exception as e:
        print("[!] Error occurred:", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

# =============================================
# HOW TO RUN
# 1. pip install selenium webdriver-manager
# 2. python selenium_automation.py
# =============================================
