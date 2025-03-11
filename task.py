import argparse
import base64
import io
import json
import smtplib
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedCond
from time import sleep
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys


import requests

res_date = datetime.datetime.now() + datetime.timedelta(days=2)

def print_with_time(msg):
    print("[{}] {}".format(time.strftime("%H:%M:%S", time.localtime()), msg))

class AutoReservation:
    def __init__(
            self,
            username,
            password,
            resvation_times,
            reservation_time: str,
            reservation_arena: str,

            capcha_username: str = None,
            capcha_password: str = None,
            receive_email: str = None,
            send_email: str = None,
            send_email_key: str = None,
            **kwargs
    ):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 启用无头模式
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver: WebDriver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.wait: WebDriverWait = WebDriverWait(
            self.driver,
            timeout=5,
        )

        self.action_chains = ActionChains(self.driver)
        self.username = username
        self.password = password
        #设置为两天后
        self.reservation_date = res_date
        self.reservation_times = resvation_times
        self.reservation_time = reservation_time
