from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

driver = webdriver.Edge()
driver.maximize_window()

driver.get('url')
driver.implicitly_wait(10)
time.sleep(5)

#data login
nama = ''
password = ''
tahun = ''
pemda  = ''

def login():
    # masukkan Username dan password
    driver.find_element(By.NAME,"username").send_keys(nama)
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div/div[2]/form/div[2]/div/input").send_keys(password)
    time.sleep(1)

    # pilih tahun
    inputTahun = driver.find_element(By.XPATH,"//input[@aria-autocomplete='list']")
    inputTahun.send_keys(tahun)
    time.sleep(1)
    inputTahun.send_keys(Keys.RETURN)

    # pilih pemda
    inputPemda = driver.find_element(By.XPATH,"//input[@aria-labelledby='vs2__combobox']")
    inputPemda.send_keys(pemda)
    inputPemda.send_keys(Keys.RETURN)
    time.sleep(2)

    # tombol login
    logIN = driver.find_element(By.XPATH,"//button[@type='submit']")
    logIN.click()
    time.sleep(2)

    # klik jurnal
    driver.get('https://bolaangmongondowselatankab.sipd.kemendagri.go.id/aklap/buku-besar')

login()

skpd = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div/div[1]/fieldset[1]/div/div/div/div/div[1]/input")
skpd.send_keys("BADAN PENANGGULANGAN BENCANA DAERAH")
skpd.send_keys(Keys.RETURN)
time.sleep(3)

klasifikasi = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div/div[1]/fieldset[2]/div/div/div/div/div[1]/input")
klasifikasi.send_keys("2. Kelompok")
klasifikasi.send_keys(Keys.RETURN)
time.sleep(4)

nm_rek = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div/div[1]/fieldset[3]/div/div/div/div/div[1]/input")
nm_rek.send_keys("BELANJA MODAL")
time.sleep(3)
nm_rek.send_keys(Keys.ENTER)


terap = driver.find_element(By.XPATH,"//button[@type='button' and contains(@class, 'btn-primary') and contains(., 'Terapkan')]")
terap.send_keys(Keys.ENTER)

cetak = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div/div[1]/fieldset[7]/div/div/div/button")
cetak.send_keys(Keys.ENTER)

excel = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div/div[1]/fieldset[7]/div/div/div/ul/li[1]/a")
excel.send_keys(Keys.ENTER)

