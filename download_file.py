from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Open Chrome
def download_file():
    opts = webdriver.ChromeOptions()
    # opts.binary_location = os.environ.get('GOOGLE_CHROME_BIN', None)
    prefs = {"download.default_directory": "/home/seluser"}
    opts.add_experimental_option("prefs", prefs)

    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    # put the path of the downloaded chrome driver executable here"
    # driver_path = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Remote("http://localhost:4444/wd/hub", options=opts)

    # Open URL
    driver.get(
        'http://demo.automationtesting.in/FileDownload.html')

    # Enter text
    driver.find_element(by=By.ID,value='textbox').send_keys("Hello world")

    # Generate Text File
    driver.find_element(by=By.ID,value='createTxt').click()

    # Click on Download Button
    driver.find_element(by=By.ID,value='link-to-download').click()
    return "Hello World"

download_file()