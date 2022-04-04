import pytest
import time
import os
import signal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestNippou():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nippou(self):
    self.driver.get("https://itb-hdb2.htdb.jp/ggutk9a/top/index")
    self.driver.set_window_size(949, 823)
    self.driver.find_element(By.ID, "loginId").send_keys("yunosuke.ide")
    self.driver.find_element(By.ID, "loginPassword").send_keys("rakus@321")
    self.driver.find_element(By.ID, "jq-loginSubmit").click()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.LINK_TEXT, "日報・月報").click()
    self.driver.find_element(By.LINK_TEXT, "日報管理DB").click()
    self.driver.find_element(By.LINK_TEXT, "日報・月報").click()
    time.sleep(1.0)
    self.driver.find_element(By.LINK_TEXT, "日報管理DB").click()
    time.sleep(1.0)
    element = self.driver.find_element(By.LINK_TEXT, "日報管理DB")
    time.sleep(1.0)
    self.driver.find_element(By.CSS_SELECTOR, "#menuli_101255 .fw-ovf-max").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.ID, "field_102279").click()
    self.driver.find_element(By.ID, "field_102279").send_keys("あ")
    self.driver.find_element(By.LINK_TEXT, "確定").click()