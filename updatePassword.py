from playwright.sync_api import sync_playwright
import time

def updatePassword(page):
    page.goto("https://adactinhotelapp.com/ChangePassword.php")
    page.fill("#current_pass", "123456")
    page.fill("#new_password", "12345")
    page.fill("#re_password", "12345")
    time.sleep(3)    
    page.click("#Submit")
    page.wait_for_load_state("networkidle")
