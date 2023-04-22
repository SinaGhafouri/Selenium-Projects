from tqdm import tqdm
import os
from glob import glob
import re
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import warnings
warnings.filterwarnings("ignore")
PATH = 'C:/Program Files/chromedriver.exe'


"""Functions"""
def open_url(url, pageLoadStrategy='eager'):
    caps = DesiredCapabilities().CHROME ; caps["pageLoadStrategy"] = pageLoadStrategy # "eager", "normal", "none"
    chrome_options = Options()  ; 
    chrome_options.headless = True
    # chrome_options.add_argument("window-size=700,800")

    driver = webdriver.Chrome(executable_path=PATH, desired_capabilities=caps, chrome_options=chrome_options)
    driver.minimize_window()
    driver.get(url)

    return driver

def get_element_by_xpath(driver, xpath):
    return driver.find_element(by=By.XPATH, value=xpath)