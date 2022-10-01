from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bot.constants import BASE_URL_


class Bot(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Bot, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_video(self, url):
        self.get(url)
        self.click_more()
        self.click_transcript_btn()
        self.get_transcript()
        


    def click_more(self):
        more = self.find_element(By.CSS_SELECTOR, 'button[aria-label="More actions"]')
        more.click()

    def click_transcript_btn(self):
        showTranscript = self.find_element(By.CLASS_NAME, 'ytd-menu-popup-renderer')
        showTranscript.click()

    def get_transcript(self):
        transcript = self.find_elements(By.CSS_SELECTOR, 'yt-formatted-string[class="segment-text style-scope ytd-transcript-segment-renderer"]')
        for line in transcript:
            print(line.text)