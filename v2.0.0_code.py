
from docx import Document
import random, os, shutil, time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

desktop_path = "C:/Users/Luck/Desktop/"

try:
    shutil.rmtree(desktop_path + 'word')
except:
    pass
try:
    os.mkdir(desktop_path + 'word')
except:
    pass

doc_types = ['brief introduction', 'translation to Chinese', 'short quiz', 'notes', 'worksheet', 'multiple choice questions', 'short questions', 'structural questions', 'fill in the blanks', 'matching questions', 'Essay-type questions']

loop_count = input('Loop count  ')

options = Options()
options.add_argument("--start-maximized")            # Window maximized to load login btn in home page
options.add_argument("--disable-popup-blocking")
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

wiki_text_list = []
for count in range(int(loop_count)):
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    old_tab = driver.current_window_handle

    wiki_text = ''
    for css_count in range(1, 30):
        try:
            wiki_text = driver.find_element(By.CSS_SELECTOR, value='#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child('+ str(css_count) + ')').text + wiki_text
        except:
            pass
    wiki_text_list.append(wiki_text)

for count in range(int(loop_count)):
    driver.switch_to.new_window('tab')
    driver.get('https://askyourpdf.com/tools/text-generator/generate')

driver.switch_to.window(old_tab)
driver.close()

def make_doc():
    tab_id_list = driver.window_handles
    wiki_text_count = 0
    for tab_id in tab_id_list:
        wiki_text_count += 1
        driver.switch_to.window(tab_id)
        input_box = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[1]/div/div[1]/textarea')
        enter_btn = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[1]/div/button')
        input_text = wiki_text_list[wiki_text_count-1] + '. Make a ' + doc_types[random.randint(0, len(doc_types)-1)] + ' about the above article.'
        input_box.send_keys(wiki_text_list[wiki_text_count-1] + '. Make a ' + doc_types[random.randint(0, len(doc_types)-1)] + ' about the above article.')
        enter_btn.click()

    for count in range(30):
        time.sleep(10)
        for tab_id in tab_id_list:
            driver.switch_to.window(tab_id)
            try:
                text_generated = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[2]/div[2]/div/pre').text
            except:
                continue
            else:
                document = Document()
                document.add_paragraph(text_generated)
                document.save(desktop_path + 'word/' + str(random.randint(1,1000)) + '.docx')
                wiki_text_list.remove(wiki_text_list[tab_id_list.index(tab_id)])
                tab_id_list.remove(tab_id)
        if not tab_id_list:
            driver.quit()
            quit()


for count in range(2):
    make_doc()

