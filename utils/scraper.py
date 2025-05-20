from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_profile_data(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    try:
        bio = soup.find('meta', property='og:description')["content"]
    except:
        bio = "Bio not found"

    try:
        profile_img = soup.find('meta', property='og:image')["content"]
    except:
        profile_img = None

    driver.quit()
    return bio, profile_img