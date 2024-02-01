from getLink import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = '/Users/abc/desktop/Nse/chromedriver-mac-arm64/chromedriver'

chrome_options = Options()
# Add any additional options as needed
#chrome_options.add_argument("--headless")

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/abc/desktop/nse/nse_xbrl",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    
})
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

for i,xbrl_link in enumerate(column_values_xbrl): 
    driver.get(xbrl_link)
    with open ("NSE_XBRL/"+ file_name[i],"w+") as f:
        f.write(driver.page_source)
        f.close()
driver.quit()
