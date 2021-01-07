import os
import time
import re
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt

class webbot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome()

    def precoGangGood(self, site):
        try:
            site = site
            self.driver.get(site)
            self.driver.implicitly_wait(30)

            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.driver.find_element_by_class_name('product-title-text').click()
            titulo = self.driver.find_element_by_class_name('product-title-text').text
            time.sleep(20)

            self.driver.find_element_by_class_name('shipping-price').click()
            frete = self.driver.find_element_by_class_name('shipping-price').text
            time.sleep(20)

            self.driver.find_element_by_class_name('main-price').click()
            preco = self.driver.find_element_by_class_name('main-price').text
            time.sleep(20)


            print("Titulo: " + data)
            print("Titulo: " + titulo)
            print("Preço : " + preco)
            print("Frete : "+ frete)
            print("--------------------")

            time.sleep(10)

            dados =  data + ';' + titulo + ';' + preco + ';' + frete
            self.salvaDados(dados)

        except:
            self.driver.close()
            self.erro()

    def erro(self):
         self.precoGangGood()

    def salvaDados(self, dados):
        #data = datetime.now().date().strftime("%Y-%m-%d")
        arquivo = open('DadosProdutos.txt', 'a')
        arquivo.write(dados + '\n')
        arquivo.close()