from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver


class Example(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "searchInput": ('CSS', 'body > table > tbody > tr:nth-child(2) > td > table:nth-child(1) > tbody > '
                               'tr:nth-child(1) > td.t1 > table > tbody > tr > td:nth-child(2) > input[type=text]'),
        "searchButton": ('CSS', 'body > table > tbody > tr:nth-child(2) > td > table:nth-child(1) > tbody > '
                                'tr:nth-child(1) > td.t1 > table > tbody > tr > td:nth-child(1) > input[type=image]'),
    }

    def open_site_search(self):
        # set_text(), click_button() methods - extended methods in PageFactory
        self.searchInput.set_text("Лоськов")
        self.searchButton.click_button()


def test_open_site_search():
    driver = webdriver.Chrome("/opt/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(6)
    driver.get("https://lokomotiv.info/")
    test = Example(driver)
    test.open_site_search()
    assert driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(2) > td > table:nth-child(2) > '
                                               'tbody > tr:nth-child(1) > td:nth-child(3) > div.hdr-lined')
    driver.quit()
