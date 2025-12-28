
#import pytest
from pages.auth_page import AuthPage

from selenium import webdriver

#driver = webdriver.Firefox()

#a = AuthPage(driver)

def test_auth_page(driver):
    page = AuthPage(driver)
    #assert page.tab_text.find() != None
    assert page.logo.is_visible()
    assert page.tab_phn.is_visible()
    assert page.tab_mal.is_visible()
    assert page.tab_log.is_visible()
    assert page.tab_ls.is_visible()
    #assert page.tab_text.is_visible()