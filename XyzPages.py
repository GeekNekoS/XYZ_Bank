from BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchTools(BasePage):

    def click_the_button(self, xpath):
        button = self.find_element((By.XPATH, xpath))
        button.click()
        return button

    def write_input(self, xpath, key):
        input_placeholder = self.find_element((By.XPATH, xpath))
        input_placeholder.send_keys(key)
        return input_placeholder

    def check_info_of_element(self, xpath):
        info = self.find_element((By.XPATH, xpath))
        return info

    def check_info_of_elements(self, xpath):
        info = self.find_elements((By.XPATH, xpath))
        return info

    def get_screenshot_as_png(self):
        photo = self.driver.get_screenshot_as_png()
        return photo
