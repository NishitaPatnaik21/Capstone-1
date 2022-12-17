import time
from selenium import webdriver
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import os


def download_zip_files(url):
    options = Options()
    # options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)

    print(f"Fetching data for : {url} \n")

    driver.get(url)
    time.sleep(10)
    accept_button = driver.find_element(
        by=By.XPATH, value="/html/body/div[4]/div/div/div/div[2]/button"
    )
    accept_button.click()

    time.sleep(4)

    # enable when to download

    # download_button = driver.find_element(
    #     by=By.XPATH, value='//*[@id="skip"]/span/div/div/div[2]/div/div[1]/button[2]'
    # )
    print(f"Downloading data from : {url} \n")
    # download_button.click()

    time.sleep(3)
    driver.close()


if __name__ == "__main__":
    urls = [
        "https://portal.gdc.cancer.gov/files/1090010a-c5b6-48d9-9fe8-0c798586096c",
        "https://portal.gdc.cancer.gov/files/f6773645-e868-494e-8d95-cd2055759682",
    ]
    for url in urls:
        download_zip_files(url)
