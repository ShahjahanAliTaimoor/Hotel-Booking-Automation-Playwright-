from playwright.sync_api import sync_playwright
import time

def searchHotel(page):
    page.goto("https://adactinhotelapp.com/SearchHotel.php")
    page.select_option("#location", label="New York")
    page.select_option("#hotels", label="Hotel Sunshine")
    page.select_option("#room_type", label="Super Deluxe")
    page.select_option("#room_nos", label="1 - One")
    page.fill("#datepick_in", "13/12/2025")
    page.fill("#datepick_out", "14/12/2025")
    time.sleep(1)    
    page.click("#Submit")

    page.goto("https://adactinhotelapp.com/SelectHotel.php") 

    page.click("#radiobutton_0")
    page.click("#continue") 
    page.fill("#first_name", "Shahjahan") 
    page.fill("#last_name", "Ali Taimoor") 
    page.fill("#address", "Karachi, Pakistan") 
    page.fill("#cc_num", "4242424242424242") 
    page.select_option("#cc_type", label="Master Card") 
    page.select_option("#cc_exp_month", label="March") 
    page.select_option("#cc_exp_year", label="2030") 
    page.fill("#cc_cvv", "123") 
    time.sleep(1)    
    page.click("#book_now") 
    page.click("#my_itinerary") 
    
    page.goto("https://adactinhotelapp.com/BookedItinerary.php")

    time.sleep(1)
    page.wait_for_load_state("networkidle")     