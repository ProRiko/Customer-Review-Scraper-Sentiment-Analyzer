from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def get_trustpilot_reviews(url, max_pages=10):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    reviews = []
    
    driver.get(url)
    time.sleep(3)  # Wait for page to load

    for _ in range(max_pages):
        review_elements = driver.find_elements(By.CLASS_NAME, "typography_body-l")
        for review in review_elements:
            reviews.append(review.text)
        
        try:
            next_button = driver.find_element(By.CLASS_NAME, "pagination-button-next")
            next_button.click()
            time.sleep(2)
        except:
            break  # No more pages

    driver.quit()
    return reviews
