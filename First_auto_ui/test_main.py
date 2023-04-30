from time import sleep
from First_auto_ui.main_page import MainPage

def test_search(driver):
    main_page = MainPage(driver)
    main_page.load()
    assert main_page.is_loaded()
    main_page.search_for_product("Iphone")
    sleep(5)
    assert driver.current_url.startswith("https://www.mvideo.ru/smartfony-i-svyaz")


