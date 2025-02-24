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
import os

site = 'https://consulta-empresa.netlify.app/'

chrome_options=Options()
chrome_options.add_experimental_option('prefs',{
    'download.prompt_for_download':False,
    'dowload.deafult_directory':r'C:\Relatorio\Relatorios',
    'profile.default_content_setting_values.automatic_download': 1,

})
driver = webdriver.Chrome(options=chrome_options)
driver.get(site)
sleep(5)


usuario = driver.find_element(By.XPATH,"//input[@id = 'username']")
sleep(1)
usuario.click()
usuario.send_keys('jhonatan')


senha = driver.find_element(By.XPATH,"//input[@id = 'password']")
sleep(1)
senha.click()
senha.send_keys('12345678')


entrar = driver.find_element(By.XPATH,"//button[@class = 'btn btn-primary btn-lg']")
entrar.click()

sleep(5)

def download_relatorios(driver):

    nomes_Empresas =  driver.find_elements(By.XPATH,"//td[@name='nome_empresa']")
    sleep(2)
    btns_download = driver.find_elements(By.XPATH,"//button[@class='download-btn']")
    sleep(2)

    for nome,botao in zip(nomes_Empresas,btns_download):
        botao.click()   
        sleep(3)

        diretorio=r'C:\Relatorio \Relatorios'  
        nome_antigo= 'perfil_empresa.pdf'
        novo_nome= f'{nome.text}.pdf'

        caminho_completo_antigo = os.path.join(diretorio,nome_antigo)
        caminho_completo_novo = os.path.join(diretorio,novo_nome)

        os.rename(caminho_completo_antigo,caminho_completo_novo)


download_relatorios(driver=driver)

btn_proximo = driver.find_element(By.XPATH,"//button[@id='nextBtn']")

while (btn_proximo.get_attribute('disable') ==None):
    btn_proximo.click()
    download_relatorios(driver=driver)

input("Pessione Qualquer tecla para fechar")