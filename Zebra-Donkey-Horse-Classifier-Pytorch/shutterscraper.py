from selenium import webdriver
# use to initialize driver in a better way without having chromedriver path mentioned.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time
import ssl

# For python2
# from urllib import urlretrieve
# import Tkinter, Tkconstants, tkFileDialog
#
# def askDialog():
#    return tkFileDialog.askdirectory()
#
# def inp(text):
#    return raw_input(text)

# For python3
from urllib.request import urlretrieve
import tkinter
import tkinter.constants
import tkinter.filedialog


def askDialog():
    return tkinter.filedialog.askdirectory()


def inp(text):
    return input(text)


ssl._create_default_https_context = ssl._create_unverified_context


def videoscrape():
    try:
        # This installs or finds the new version of chrome driver if not available and links to path automatically.
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        for i in range(1, searchPage + 1):
            url = "https://www.shutterstock.com/video/search/" + \
                searchTerm + "?page=" + str(i)
            driver.get(url)
            print("Page " + str(i))
            for j in range(0, 50):
                while True:
                    container = driver.find_elements_by_xpath(
                        "//div[@data-automation='VideoGrid_video_videoClipPreview_" + str(j) + "']")
                    if len(container) != 0:
                        break
                    if len(driver.find_elements_by_xpath("//div[@data-automation='VideoGrid_video_videoClipPreview_" + str(j + 1) + "']")) == 0 and i == searchPage:
                        driver.close()
                        return
                    time.sleep(10)
                    driver.get(url)
                container[0].click()
                while True:
                    wait = WebDriverWait(driver, 60).until(ec.visibility_of_element_located(
                        (By.XPATH, "//video[@data-automation='VideoPlayer_video_video']")))
                    video_url = driver.current_url
                    data = driver.execute_script(
                        "return document.documentElement.outerHTML")
                    scraper = BeautifulSoup(data, "lxml")
                    video_container = scraper.find_all(
                        "video", {"data-automation": "VideoPlayer_video_video"})
                    if len(video_container) != 0:
                        break
                    time.sleep(10)
                    driver.get(video_url)
                video_array = video_container[0].find_all("source")
                video_src = video_array[1].get("src")
                name = video_src.rsplit("/", 1)[-1]
                try:
                    urlretrieve(video_src, os.path.join(
                        scrape_directory, os.path.basename(video_src)))
                    print("Scraped " + name)
                except Exception as e:
                    print(e)
                driver.get(url)
    except Exception as e:
        print(e)


def imagescrape():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(ChromeDriverManager().install(
        ), options=chrome_options)  # chrome_options is deprecated
        driver.maximize_window()
        for i in range(1, searchPage + 1):
            url = "https://www.shutterstock.com/search?searchterm=" + searchTerm + "&sort=popular&image_type=" + \
                image_type + \
                "&search_source=base_landing_page&language=en&page=" + str(i)
            driver.get(url)
            # Scroll to the bottom of the page
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            # Wait 4 seconds for all the images to load
            time.sleep(4)
            data = driver.execute_script(
                "return document.documentElement.outerHTML")
            print("Page " + str(i))
            scraper = BeautifulSoup(data, "lxml")
            img_container = scraper.find_all(
                "img", {"class": "z_h_9d80b z_h_2f2f0"})
            for j in range(0, len(img_container)-1):
                img_src = img_container[j].get("src")
                name = img_src.rsplit("/", 1)[-1]
                try:
                    urlretrieve(img_src, os.path.join(
                        scrape_directory, os.path.basename(img_src)))
                    print("Scraped " + name)
                except Exception as e:
                    print(e)
        driver.close()
    except Exception as e:
        print(e)


print("ShutterScrape")

#scrape_directory = "C:/Users/[username]/[path]"

while True:
    while True:
        print("Please select a directory to save your scraped files.")
        scrape_directory = askDialog()
        if scrape_directory == None or scrape_directory == "":
            print("You must select a directory to save your scraped files.")
            continue
        break
    while True:
        searchMode = inp("Search mode ('v' for video or 'i' for image): ")
        if searchMode != "v" and searchMode != "i":
            print("You must select 'v' for video or 'i' for image.")
            continue
        break
    if searchMode == 'i':
        while True:
            image_type = inp(
                "Select image type ('a' for all or 'p' for photo): ")
            if image_type != "a" and image_type != "p":
                print("You must select 'a' for all or 'p' for photo.")
                continue
            break
        if image_type == 'p':
            image_type = 'photo'
        else:
            image_type = 'all'
    while True:
        searchCount = int(inp("Number of search terms: "))
        if searchCount < 1:
            print("You must have at least one search term.")
            continue
        elif searchCount == 1:
            searchTerm = inp("Search term: ")
        else:
            searchTerm = inp("Search term 1: ")
            for i in range(1, searchCount):
                searchTermPart = inp("Search term " + str(i + 1) + ": ")
                if searchMode == "v":
                    searchTerm += "-" + searchTermPart
                if searchMode == "i":
                    searchTerm += "+" + searchTermPart
        break
    while True:
        searchPage = int(input("Number of pages to scrape: "))
        if searchPage < 1:
            print("You must have scrape at least one page.")
            continue
        break
    if searchMode == "v":
        videoscrape()
    if searchMode == "i":
        imagescrape()
    print("Scraping complete.")
    restartScrape = inp("Keep scraping? ('y' for yes or 'n' for no) ")
    if restartScrape == "n":
        print("Scraping ended.")
        break
