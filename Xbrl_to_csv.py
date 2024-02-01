from getLink import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = '/Users/abc/desktop/Nse/chromedriver-mac-arm64/chromedriver'

chrome_options = Options()

#chrome_options.add_argument("--headless")

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/abc/desktop/nse/nse_xlsx",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    
})
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

for name in file_name:
    driver.get("http://ec2-3-221-41-38.compute-1.amazonaws.com/")
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="FileUploadControl"]'))
    )
    file_input.send_keys(f"/Users/abc/desktop/nse/nse_xbrl/{name}")
    unhide_script = "document.getElementById('Button1').style.display = 'block';"
    driver.execute_script(unhide_script)
    time.sleep(4)
    driver.execute_script("document.getElementById('Button1').click();")
    
