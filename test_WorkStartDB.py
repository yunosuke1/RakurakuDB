import pytest
import time
import os
import signal
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestWorkStartDB():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_workStartDB(self):
    comment_list=["Selenium学習","Python学習","CircleCI学習","Jenkins学習","Cypress学習"]
    rand=random.randint(0,4)
    self.driver.get("https://itb-hdb2.htdb.jp/ggutk9a/top/index")
    self.driver.set_window_size(982, 821)
    self.driver.find_element(By.ID, "loginId").send_keys("yunosuke.ide")
    self.driver.find_element(By.ID, "loginPassword").send_keys("rakus@321")
    self.driver.find_element(By.ID, "jq-loginSubmit").click()
    
    self.driver.switch_to.frame(1)
    time.sleep(1.0)
    self.driver.find_element(By.CSS_SELECTOR, "#nav-dbg-100026 .fw-ovf-max").click()
    time.sleep(1.0)
    self.driver.find_element(By.CSS_SELECTOR, "#nav-db-100539 .fw-ovf-max").click()
    time.sleep(1.0)
    self.driver.find_element(By.CSS_SELECTOR, "#menuli_101055 .fw-ovf-max").click()
    time.sleep(1.0)

    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)

    self.driver.find_element(By.ID, "field_103738").click()
    self.driver.find_element(By.ID, "field_103738").send_keys(comment_list[rand])
    self.driver.find_element_by_class_name("fw-btn-ok fw-btn-icon fw-mw100").click()