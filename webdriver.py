from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class WebDriver:

    def enter_website(self, outbound, destination, outbound_date, return_date):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver_path = "/Users/ianperry/Documents/python/chromedriver"
        driver = webdriver.Chrome(options=chrome_options)

        outbound_date = outbound_date.split("T")[0]
        return_date = return_date.split("T")[0]

        url = (f"https://www.kiwi.com/en/?sortBy=duration"
               f"&inboundDate={return_date}"
               f"&outboundDate={outbound_date}"
               f"&destination={destination}"
               f"&origin={outbound}")

        driver.get(url)
        # time.sleep(10)
        #
        # button = driver.find_element(By.XPATH, '//*[@id="HomePage"]/div[2]/div[2]/div[2]/div/div[2]/a/div/div')
        # button.click()
