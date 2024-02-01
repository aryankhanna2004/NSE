from getLink import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = '/Users/abc/desktop/Nse/chromedriver-mac-arm64/chromedriver'

chrome_options = Options()
# Add any additional options as needed
#chrome_options.add_argument("--headless")


chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/abc/desktop/nse/nse_pdf",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # Open PDFs in an external application
})
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
for pdf_link in column_values_pdf: 
    driver.get(pdf_link)
driver.quit()






