import time
from selenium import webdriver
from booking.bookingFiltration import BookingFiltration
import booking.constants as Cste
from prettytable import PrettyTable
from selenium.webdriver.common.by import By

hotel_descriptions=[]

class Booking(webdriver.Chrome):
    def __init__(self, driver_path,teardown=False):
        self.teardown=teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',["enable-logging"])
        super().__init__(driver_path,chrome_options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def change_currency(self,currency=None):
        currency_btn = self.find_element(by=By.CSS_SELECTOR,value='button[data-tooltip-text="Choisissez votre devise"]')
        currency_btn.click()
        select_currency= self.find_element(by=By.CSS_SELECTOR,value=f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        select_currency.click()

    def enter_city(self,city):
        city_input=self.find_element_by_id("ss")
        city_input.clear()
        city_input.send_keys(city)
        choose_city= self.find_element(by=By.CSS_SELECTOR,value="li[data-i='0']")
        choose_city.click()

    def choose_check_it_out_date(self, checkin,checkout):
        ckeckin_date_btn= self.find_element(by=By.CSS_SELECTOR,value=f"td[data-date='{checkin}']")
        ckeckin_date_btn.click()
        checkout_date_btn=self.find_element(by=By.CSS_SELECTOR,value=f"td[data-date='{checkout}']")
        checkout_date_btn.click()

    def Add_adult(self,number):
        display_options= self.find_element_by_id("xp__guests__toggle")
        display_options.click()
        cursor_style=''
        while cursor_style!='not-allowed':
            reduce_adult_btn=self.find_element(by=By.CSS_SELECTOR,value="button[aria-label='Supprimer des Adultes']")        
            cursor_style= reduce_adult_btn.value_of_css_property('cursor')
            reduce_adult_btn.click()
            time.sleep(1)
        add_adult_btn=self.find_element(by=By.CSS_SELECTOR,value="button[aria-label='Ajouter des Adultes']")        
        for _ in range(number-1):
            add_adult_btn.click()

    def view_results(self):
        display_results= self.find_element(by=By.CSS_SELECTOR,value="button[data-sb-id='main']")
        display_results.click()

    def land_first_age(self):
        self.get(f'{Cste.url_booking}')

    def do_filration(self):
        filtrations = BookingFiltration(self)
        filtrations.filter_by_rating(5)
  
    def report_result(self):
        list_results = self.find_elements(by=By.CSS_SELECTOR,value='div[data-testid="property-card"]')
        for hotel in list_results:
            hotel_names= hotel.find_element(by=By.CSS_SELECTOR,value='div[data-testid="title"]')
            hotel_price= hotel.find_element(by=By.CSS_SELECTOR,value='span[class="fcab3ed991 bd73d13072"]')
            hotel_descp=[hotel_names.get_attribute("innerHTML").strip(),' '.join(hotel_price.get_attribute("innerHTML").split("&nbsp;")).strip()]
            hotel_descriptions.append(hotel_descp)
        table = PrettyTable(field_names=["hotel name", "hotel price"])
        table.add_rows(hotel_descriptions)
        print(table)

    def __exit__(self, *args):
        if self.teardown:
            self.quit()
    
    