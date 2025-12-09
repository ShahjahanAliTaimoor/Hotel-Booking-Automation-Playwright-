from playwright.sync_api import sync_playwright
import time

def registerPage(page):
    page.goto("https://adactinhotelapp.com/Register.php")
    page.fill("#username", "ShahjahanAT")
    page.fill("#password", "123456")
    page.fill("#re_password", "123456")
    page.fill("#full_name", "Shahjahan Ali Taimoor")
    page.fill("#email_add", "shahjahan.baig2000@gmail.com")
    input("Solve CAPTCHA then press Enter...")
    page.check("#tnc_box")
    time.sleep(1)
    page.click("#Submit")
    page.wait_for_load_state("networkidle")