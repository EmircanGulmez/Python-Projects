'''
instagram'a giriş yapar, tüm takipçi listelerini alır, otomatik takip eder veya bırakır ve 
takipçileri dosyaya kayıt eder
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class instagram:
    def __init__(self, kullanici, sifre):
        self.browser = webdriver.Chrome()

        self.kullanici = kullanici
        self.sifre = sifre

        takipcilerKullanici = []
        takipcilerIsim = []

        takipKullanici = []
        takipIsim = []

    def giris(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(3)

        kullaniciGiris = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        sifreGiris = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        kullaniciGiris.send_keys(self.kullanici)
        sifreGiris.send_keys(self.sifre)
        sifreGiris.send_keys(Keys.ENTER)
        time.sleep(2)
        
        
    
    def takipciSayfasi(self):
        self.browser.get(f"https://www.instagram.com/{self.kullanici}")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div").click()
        time.sleep(1)

        takipciler = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
        for i in takipciler:
            durum = i.find_element_by_css_selector("a").get_attribute("href")
            print(durum)

insta = instagram("out.i.s", "03031980789enes")
insta.giris()
time.sleep(2)
insta.takipciSayfasi()
time.sleep(5)
insta.browser.close()