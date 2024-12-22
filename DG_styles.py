from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.digistyle.com/")

product = input("What do you want tp buy ?")

search_box1 = driver.find_element(By.CSS_SELECTOR, "input.c-mega-search__input")
search_box1.send_keys(product,Keys.ENTER)

product_cards = driver.find_elements(By.CSS_SELECTOR, ".cp-card")


for card in product_cards:
        try:
            title_element = card.find_element(By.CSS_SELECTOR, "a.c-product-card__brand")
            price_element = card.find_element(By.CSS_SELECTOR, ".c-product-card__discount")
            link_element = card.find_element(By.CSS_SELECTOR, "a.c-product-card__image-container")

            print(f"Title: {title_element.text}")
            print(f"Price: {price_element.text}")
            print(f"Link: {link_element.get_attribute('href')}")
            print("-" * 4)
        except Exception as e:
            print(f"An error occurred while processing a product: {e}")





