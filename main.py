from playwright.sync_api import sync_playwright
import time
from loginPage import loginPage
from searchHotel import searchHotel 
from updatePassword import updatePassword

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()

        loginPage(page)
        searchHotel(page)
        updatePassword(page)
        page.click("text=Logout")
        time.sleep(1)
        
        context.close()
        browser.close()

if __name__ == "__main__":
    main()
