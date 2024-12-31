from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import webbrowser
from googletrans import Translator


translator = Translator()

window = tk.Tk()
window.title("movie links")
window.geometry('700x450')

lable1 = tk.Label(window, text="What do you want to see?",font=('tahoma',20),width=30,height=4)
lable1.pack()
entry1 = tk.Entry(window, width=30, font=('tahoma', 15))
entry1.pack()


def search_movie():
    movie_name = entry1.get()
    # translated = translator.translate(movie_name, src='auto', dest='en')
    # movie_name_translated = translated.text
    search_field = driver.find_element(By.CSS_SELECTOR, '.search input')
    search_field.send_keys(movie_name)
    search_field.send_keys(Keys.RETURN)

    search_url = driver.current_url + "search/" + movie_name
    driver.get(search_url)

    movie_title = driver.find_element(By.CSS_SELECTOR, '.title a')
    print(movie_title.text)

    button = driver.find_element(By.CLASS_NAME, 'more-link')
    button.click()

    movie_page = driver.find_element(By.CSS_SELECTOR, ".title a")
    movie_page.click()

    movie_link = driver.find_element(By.CSS_SELECTOR, "a[href*='embed']")
    mooviee = movie_link.get_attribute('href')

    def open_link(event):
        webbrowser.open_new(mooviee)

    lable3 = tk.Label(window, text=mooviee, font=('tahoma', 10), fg="blue", cursor="hand2",width=100,height=3)
    lable3.pack()
    lable3.bind("<Button-1>", open_link)



search_button = tk.Button(window, text="Search", command=search_movie)
search_button.pack()

lable2 = tk.Label(window, text="Here is the link:", font=('tahoma', 20), width=30, height=6)
lable2.pack()


driver = webdriver.Firefox()
driver.get("https://www.film2movie.asia/")


window.mainloop()
