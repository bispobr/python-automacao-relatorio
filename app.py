from ast import Pass
from email.policy import default
from gc import disable
from profile import Profile
import site
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

site = 'https://consulta-empresa.netlify.app/'

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'dowload.deafult_directory': r'C:\Relatorio\Relatorios',
    'profile.default_content_setting_values.automatic_download': 1,

})
driver = webdriver.Chrome(options=chrome_options)
driver.get(site)
sleep(5)


usuario = driver.find_element(By.XPATH, "//input[@id = 'username']")
sleep(1)
usuario.click()
usuario.send_keys('jhonatan')


senha = driver.find_element(By.XPATH, "//input[@id = 'password']")
sleep(1)
senha.click()
senha.send_keys('12345678')


entrar = driver.find_element(
    By.XPATH, "//button[@class = 'btn btn-primary btn-lg']")
entrar.click()
