from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from bs4 import BeautifulSoup
import requests
import pyautogui as ptg
import unittest


PATH = "C:\Program Files (x86)\chromedriver.exe"
SRC = requests.get("https://mbasic.facebook.com/atisaviationacademic/").text
SOUP = BeautifulSoup(SRC, 'lxml')

driver = webdriver.Chrome(PATH)
driver.get("https://mbasic.facebook.com/atisaviationacademic/")
#driver.execute_script("window.scrollBy(0,1500)")

email = "fbcrawler888@gmail.com"
password = "farabischool2"

log_in_btn_1 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/a[2]").click()
#email_input_btn = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div[2]/form/ul/li[1]/input").click()


#Point(x=325, y=234) // email coords
#Point(x=588, y=303) // pass coords
ptg.click(325, 234)
ptg.typewrite(email, interval=0.05)
ptg.click(588, 303)
ptg.typewrite(password, interval=0.05)

log_in_btn_2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div[2]/form/ul/li[3]/input").click()

#Point(x=1188, y=59) // URL area

post_link = "https://mbasic.facebook.com/story.php?story_fbid=4047292948675740&id=162789910459416&refid=17&_ft_=mf_story_key.4047292948675740%3Atop_level_post_id.4047292948675740%3Atl_objid.4047292948675740%3Acontent_owner_id_new.162789910459416%3Athrowback_story_fbid.4047292948675740%3Apage_id.162789910459416%3Aphoto_id.4047292888675746%3Astory_location.4%3Astory_attachment_style.photo%3Atds_flgs.3%3Apage_insights.%7B%22162789910459416%22%3A%7B%22page_id%22%3A162789910459416%2C%22page_id_type%22%3A%22page%22%2C%22actor_id%22%3A162789910459416%2C%22dm%22%3A%7B%22isShare%22%3A0%2C%22originalPostOwnerID%22%3A0%7D%2C%22psn%22%3A%22EntStatusCreationStory%22%2C%22post_context%22%3A%7B%22object_fbtype%22%3A266%2C%22publish_time%22%3A1595161630%2C%22story_name%22%3A%22EntStatusCreationStory%22%2C%22story_fbid%22%3A%5B4047292948675740%5D%7D%2C%22role%22%3A1%2C%22sl%22%3A4%2C%22targets%22%3A%5B%7B%22actor_id%22%3A162789910459416%2C%22page_id%22%3A162789910459416%2C%22post_id%22%3A4047292948675740%2C%22role%22%3A1%2C%22share_id%22%3A0%7D%5D%7D%7D%3Athid.162789910459416%3A306061129499414%3A2%3A0%3A1596265199%3A-6263951252710306524&__tn__=%2As-R"

ptg.click(537, 75)
ptg.typewrite(post_link)
ptg.typewrite(["enter"])


all_accounts = driver.find_elements_by_class_name("eb bi")
