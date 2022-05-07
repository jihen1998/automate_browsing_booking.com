from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self,driver : WebDriver):
        self.driver=driver
    
    def filter_by_rating(self,star_value):
        star_filtration_box= self.driver.find_element(by=By.CSS_SELECTOR,value="div[data-filters-group='class']")
        star_child_filtration= star_filtration_box.find_elements(by=By.CSS_SELECTOR,value="*")
        for star_element in star_child_filtration:
            if str(star_element.get_attribute("innerHTML")).strip() == f'{star_value} étoiles':
                star_element.click()
