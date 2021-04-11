from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver


class Example(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    # Elements dictionary where key name will become WebElement using PageFactory
    elements = {
        "searchInput": ('CSS', 'body > table > tbody > tr:nth-child(2) > td > table:nth-child(1) > tbody > '
                               'tr:nth-child(1) > td.t1 > table > tbody > tr > td:nth-child(2) > input[type=text]'),
        "searchButton": ('CSS', 'body > table > tbody > tr:nth-child(2) > td > table:nth-child(1) > tbody > '
                                'tr:nth-child(1) > td.t1 > table > tbody > tr > td:nth-child(1) > input[type=image]'),
    }

    def open_site_search(self):
        # set_text(), click_button() - extended methods in PageFactory
        self.searchInput.set_text("Лоськов")
        self.searchButton.click_button()


def test_open_site_search():
    driver = webdriver.Chrome("/opt/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://lokomotiv.info/")
    test = Example(driver)
    test.open_site_search()
    assert driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(2) > td > table:nth-child(2) > '
                                               'tbody > tr:nth-child(1) > td:nth-child(3) > div.hdr-lined')
    driver.quit()
