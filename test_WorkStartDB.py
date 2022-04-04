import pytest
import time
import os
import signal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://itb-hdb2.htdb.jp/ggutk9a/top/index")
driver.set_window_size(982, 821)
driver.find_element(By.ID, "loginId").send_keys("yunosuke.ide")
driver.find_element(By.ID, "loginPassword").send_keys("rakus@321")
driver.find_element(By.ID, "jq-loginSubmit").click()
driver.switch_to.frame(1)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#nav-dbg-100026 .fw-ovf-max").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#nav-db-100539 .fw-ovf-max").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#menuli_101055 .fw-ovf-max").click()
time.sleep(1)

driver.switch_to.default_content()
driver.switch_to.frame(2)
driver.find_element(By.CSS_SELECTOR, ".fw-ff-mono").click()
driver.find_element(By.CSS_SELECTOR, ".fw-ff-mono").send_keys("Selenium")