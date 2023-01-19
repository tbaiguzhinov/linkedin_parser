import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(email, password):
    options = Options()
    options.add_argument('--excludeSwitches')
    options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    browser.get('https://www.linkedin.com/')

    email_input = browser.find_element(By.ID, 'session_key')
    email_input.send_keys(email)
    password_input = browser.find_element(By.ID, 'session_password')
    password_input.send_keys(password, Keys.RETURN)

    browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
    html = browser.find_element(By.TAG_NAME, 'html')
    
    connections_found = 1
    total_connections = {connections_found: 1}

    while total_connections[connections_found] < 5:
        try:
            button = browser.find_element(By.CLASS_NAME, 'scaffold-finite-scroll__load-button')
            button.click()
            main_text = browser.find_element(By.CLASS_NAME, 'scaffold-finite-scroll__content').get_attribute('innerHTML')
            soup = BeautifulSoup(main_text, 'lxml')
            connections_found = len(soup.find_all('li'))
            # total_connections = int(browser.find_element(By.CLASS_NAME, 't-black').text.split(' ')[0].replace(',', ''))
        except NoSuchElementException:
            html.send_keys(Keys.END)
            time.sleep(1)
        finally:
            if connections_found not in total_connections:
                total_connections[connections_found] = 0
            total_connections[connections_found] += 1
    return main_text
