import chromedriver_binary
import time
import os
import signal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

try:
  driver.get("https://itb-hdb2.htdb.jp/ggutk9a/top/index")
  driver.set_window_size(949, 823)
  driver.find_element(By.ID, "loginId").send_keys("yunosuke.ide")
  driver.find_element(By.ID, "loginPassword").send_keys("rakus@321")
  driver.find_element(By.ID, "jq-loginSubmit").click()
  driver.switch_to.frame(1)

  driver.find_element(By.LINK_TEXT, "日報・月報").click()
  time.sleep(1.0)

  driver.find_element(By.LINK_TEXT, "日報管理DB").click()
  time.sleep(1.0)

  element = driver.find_element(By.LINK_TEXT, "日報管理DB")
  time.sleep(1.0)

  driver.find_element(By.CSS_SELECTOR, "#menuli_101255 .fw-ovf-max").click()
  driver.switch_to.default_content()
  driver.switch_to.frame(2)
  
  driver.find_element(By.ID, "field_102279").click()
  driver.find_element(By.ID, "field_102279").send_keys("あ")
  driver.find_element(By.LINK_TEXT, "確定").click()
finally:
    os.kill(driver.service.process.pid,signal.SIGTERM)  
