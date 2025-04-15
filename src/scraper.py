# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import os



def get_reviews_from_amazon(url, max_reviews=10):
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')  # Anti-bot detection
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    reviews = []

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-hook='review']"))
        )

        review_blocks = driver.find_elements(By.CSS_SELECTOR, "div[data-hook='review']")
        print(f"🔍 Found {len(review_blocks)} review blocks")

        for block in review_blocks:
            try:
                text = block.find_element(By.CSS_SELECTOR, "span[data-hook='review-body']").text.strip()
                if text:
                    reviews.append(text)
            except:
                continue
            if len(reviews) >= max_reviews:
                break

    except Exception as e:
        print(f"Error while scraping reviews: {e}")

    finally:
        driver.quit()

    return reviews

def save_reviews_to_json(reviews, filename="data/raw_reviews.json"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(reviews)} reviews to {filename}")


if __name__ == "__main__":
    product_url = "https://www.amazon.com/product-reviews/B07FZ8S74R/"  # Replace with your URL
    reviews = get_reviews_from_amazon(product_url)
    save_reviews_to_json(reviews)
    print("Scraping completed.")
    print(f"Extracted {len(reviews)} reviews.")