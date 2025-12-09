from playwright.sync_api import sync_playwright
import time

def loginPage(page):
    page.goto("https://adactinhotelapp.com/")
    page.fill("#username", "ShahjahanAT")
    page.fill("#password", "123456")
    page.click("#login")
    page.wait_for_load_state("networkidle")
