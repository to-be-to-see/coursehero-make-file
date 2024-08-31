
from docx import Document
import time, random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait

desktop_path = "C:/xxxxx/Desktop/"

doc_types = ['short quiz', 'notes', 'multiple choice questions', 'short questions', 'structural questions', 'fill in the blanks questions', 'matching questions']
physics_topics = ["Classical Mechanics", "Thermodynamics", "Electromagnetism", "Optics", "Relativity", "Quantum Mechanics", "Statistical Mechanics", "Nuclear Physics", "Condensed Matter Physics", "Particle Physics", "Astrophysics", "Cosmology"]
chemistry_topics = ["Stoichiometry", "Thermodynamics", "Kinetics", "Electrochemistry", "Spectroscopy", "Acid-Base Chemistry", "Organic Chemistry", "Biochemistry", "Nuclear Chemistry", "Analytical Chemistry"]
biology_topics = ["Anatomy", "Biochemistry", "Botany", "Cell Biology", "Ecology", "Embryology", "Entomology", "Environmental Science", "Evolution", "Genetics", "Histology", "Immunology", "Microbiology", "Molecular Biology", "Neuroscience", "Pathology", "Pharmacology", "Physiology", "Taxonomy", "Zoology"]

subject_choice = input('1. Physics 2. Chemistry 3. Biology')
loop_count = input('Loop count  ')

options = Options()
#options.add_experimental_option("detach", True)     # Keep window opened when Error raised
options.add_argument("--start-maximized")            # Window maximized to load login btn in home page
options.add_argument("--disable-popup-blocking")
#options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get('https://askyourpdf.com/tools/text-generator/generate')
driver.implicitly_wait(30)

input_box = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[1]/div/div[1]/textarea')
enter_btn = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[1]/div/button')

for count in range(int(loop_count)):
    input_box.clear()
    if subject_choice == 1:
        input_box.send_keys("Make " +doc_types[random.randint(0, len(doc_types)-1)]+ " about "+random.choice(physics_topics))
    if subject_choice == 2:
        input_box.send_keys("Make " +doc_types[random.randint(0, len(doc_types)-1)]+ " about "+random.choice(chemistry_topics))
    else:
        input_box.send_keys("Make " +doc_types[random.randint(0, len(doc_types)-1)]+ " about "+random.choice(biology_topics))

    enter_btn.click()
    text_generated = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[2]/div[2]/div/pre').text

    document = Document()
    document.add_paragraph(text_generated)
    document.save(desktop_path + 'word/' + str(count) + '.docx')


driver.quit()
