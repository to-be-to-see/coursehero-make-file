
from docx import Document
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

desktop_path = "C:/input your path/Desktop/"

doc_types = ['short quiz', 'notes', 'worksheet','multiple choice questions', 'short questions', 'structural questions', 'fill in the blanks', 'matching questions', 'Essay-type questions']

physics_topics = ["Mechanics", "Thermodynamics", "Electricity", "Magnetism", "Optics", "Quantum Mechanics", "Relativity", "Acoustics", "Nuclear Physics", "Condensed Matter Physics", "Particle Physics", "Astrophysics", "Biophysics", "Geophysics", "Plasma Physics", "Electromagnetism", "Classical Mechanics", "Statistical Mechanics", "Fluid Dynamics", "Aerodynamics", "Hydrodynamics", "Electronics", "Optoelectronics", "Photonics", "Crystallography", "Materials Science", "Computational Physics", "Theoretical Physics", "Experimental Physics", "Atomic Physics", "Molecular Physics", "Chemical Physics", "Radiation Physics", "Medical Physics", "Neurophysics", "Computational Neuroscience", "Astrobiology", "Cosmology", "Gravitation", "Quantum Field Theory", "String Theory", "Fractals", "Chaos Theory", "Complexity Science", "Biomechanics", "Mechatronics", "Robotics", "Engineering Physics", "Radiation Detection", "Materials Engineering", "Nanotechnology", "Microelectronics", "Semiconductor Physics", "Superconductivity", "Superfluidity"]
chemistry_topics = [ "Stoichiometry", "Inorganic Chemistry", "Materials Science", "Organic Chemistry", "Analytical Chemistry", "Biochemistry", "Physical Chemistry", "Nuclear Chemistry", "Green Chemistry", "Surface Chemistry", "Computational Chemistry", "Environmental Chemistry", "Polymer Chemistry", "Quantum Chemistry", "Electrochemistry", "Catalysis", "Photochemistry", "Chemical Thermodynamics", "Chemical Kinetics", "Synthesis and Design", "Chemical Bonding", "Molecular Geometry", "Acid-Base Theory", "Spectroscopy", "Chromatography", "Separation Science", "Mass Spectrometry", "Computational Methods", "Toxicology", "Forensic Chemistry", "Ionic Equilibrium", "Combination Reactions", "Hydrocarbon Chemistry", "Reaction Mechanisms", "Coordination Chemistry", "Metallurgy", "Biophysical Chemistry", "Solid-State Chemistry", "Supramolecular Chemistry", "Cosmetic Chemistry", "Food Chemistry", "Cluster Chemistry", "Medicinal Chemistry", "Pharmacology", "Textile Chemistry", "Cosmochemistry", "Astrochemistry", "Molecular Biology", "Heterocyclic Chemistry" ]
biology_topics = ["Cell Biology", "Molecular Biology", "Genetics", "Evolutionary Biology", "Microbiology", "Ecology", "Botany", "Zoology", "Physiology", "Biochemistry", "Anatomy", "Developmental Biology", "Neuroscience", "Immunology", "Pharmacology", "Bioinformatics", "Biotechnology", "Marine Biology", "Evolutionary Developmental Biology", "Plant Physiology", "Mycology", "Entomology", "Ornithology", "Herpetology", "Biophysics", "Population Genetics", "Behavioral Ecology", "Conservation Biology", "Synthetic Biology", "Genomic Medicine", "Cell Signal Transduction", "Stem Cell Biology", "Evolutionary Ecology", "Ethology", "Microbial Ecology", "Physiological Ecology", "Endocrinology", "Chemical Ecology", "Aquatic Biology", "Human Biology", "Tropical Biology", "Bioethics", "Environmental Biology", "Infectious Diseases", "Comparative Anatomy", "Virology", "Evolutionary Psychology", "Ecological Genetics", "Agricultural Biology"]
maths_topics = ["Algebra", "Geometry", "Calculus", "Trigonometry", "Statistics", "Probability", "Combinatorics", "Graph Theory", "Number Theory", "Topology", "Measure Theory", "Complex Analysis", "Differential Equations", "Linear Algebra", "Mathematical Physics", "Optimization", "Operations Research", "Computational Mathematics", "Numerical Analysis", "Abstract Algebra", "Real Analysis", "Functional Analysis", "Partial Differential Equations", " Dynamical Systems", "Mathematical Biology", "Mathematical Finance", "Stochastic Processes", "Signal Processing", "Control Theory", "Information Theory", "Cryptography", "Computational Geometry", "Machine Learning", "Artificial Intelligence", "Data Mining", "Data Science", "Mathematical Modeling", "Simulation", "Game Theory", "Decision Theory", "Utility Theory", "Social Choice Theory", "Econometrics", "Mathematical Economics", "Actuarial Science", "Financial Mathematics", "Biostatistics", "Computational Statistics", "Survival Analysis", "Time Series Analysis", "Spatial Statistics", "Network Science", "Computational Neuroscience", "Mathematical Psychology", "Mathematical Sociology"]
economic_topics = ["Gross Domestic Product", "Inflation Rate", "Fiscal Policy", "Monetary Policy", "Supply and Demand", "Economic Growth", "International Trade", "Balance of Payments", "Exchange Rates", "Gini Coefficient", "Poverty Line", "Human Development Index", "Productivity Paradox", "Economic Inequality", "Market Failure", "Externalities", "Public Goods", "Opportunity Cost", "Sunk Cost", "Economies of Scale", "Comparative Advantage", "Absolute Advantage", "Trade Agreements", "Tariffs", "Quotas", "Subsidies", "Dumping", "Protectionism", "Free Trade", "Laffer Curve", "Phillips Curve", "Okun's Law", "Economic Indicators", "GDP Deflator", "Consumer Price Index", "Purchasing Power Parity", "Interest Rates", "Money Supply", "Fiscal Deficit", "National Debt", "Budget Deficit", "Monetarism", "Keynesian Economics", "Classical Economics", "Marxian Economics", "Austrian Economics", "Economic Systems", "Command Economy", "Market Economy", "Mixed Economy", "Resource Allocation", "Scarcity", "Opportunity Cost", "Economic Development", "Economic Efficiency", "Economic Justice", "Economic Freedom"]
geology_topics = ["Plate Tectonics", "Rock Cycle", "Earthquakes", "Volcanology", "Geologic Time Scale", "Folding and Faulting", "Weathering and Erosion", "Glaciers", "Groundwater", "Soil Formation", "Metamorphism", "Petrology", "Structural Geology", "Seismology", "Geomorphology", "Geophysics", "Geochemistry", "Mineralogy", "Paleontology", "Hydrogeology", "Engineering Geology", "Environmental Geology", "Geologic Hazards", "Landform Evolution", "Geothermal Energy", "Natural Resources", "Geologic Mapping", "Geologic History", "Tectonic Plate Boundaries", "Continental Drift", "Sea-Floor Spreading", "Hot Spots", "Geysers", "Caves", "Karst Topography", "Deltas", "Canons", "Waterfalls", "Geologic Processes", "Land Subsidence", "Geologic Risks", "Geologic Storage", "Carbon Sequestration", "Fracking", "Geothermal Systems", "Geologic Modeling", "Geologic Remote Sensing", "Geologic GIS", "Geologic Databases", "Geologic Informatics", "Earth's Interior", "Mantle Convection", "Core-Mantle Interaction", "Geologic Fieldwork", "Geologic Laboratory", "Geologic Computing", "Geologic Software", "Geologic Data Analysis"]


subject_choice = input('1. Physics 2. Chemistry 3. Biology 4. Maths 5. Economic 6. Geology')
loop_count = input('Loop count  ')

options = Options()
options.add_argument("--start-maximized")            # Window maximized to load login btn in home page
options.add_argument("--disable-popup-blocking")
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get('https://askyourpdf.com/tools/text-generator/generate')
driver.implicitly_wait(60)

input_box = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[1]/div/div[1]/textarea')
enter_btn = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[1]/div/button')

count = 0
while 1:
    count += 1
    if count >= int(loop_count):
        break
    input_box.clear()
    input_text1, input_text2= 'Introduce another concept in ', '. Make ' + doc_types[random.randint(0, len(doc_types)-1)] + ' about it'

    if subject_choice == '1':
        input_box.send_keys(input_text1 + random.choice(physics_topics) + input_text2)
    if subject_choice == '2':
        input_box.send_keys(input_text1 + random.choice(chemistry_topics) + input_text2)
    if subject_choice == '3':
        input_box.send_keys(input_text1 + random.choice(biology_topics) + input_text2)
    if subject_choice == '4':
        input_box.send_keys(input_text1 + random.choice(maths_topics) + input_text2)
    if subject_choice == '5':
        input_box.send_keys(input_text1 + random.choice(economic_topics) + input_text2)
    if subject_choice == '6':
        input_box.send_keys(input_text1 + random.choice(geology_topics) + input_text2)
    try:
        enter_btn.click()
        text_generated = driver.find_element(By.XPATH, value='//*[@id="__next"]/section/div[2]/div[2]/div[2]/div/pre').text
    except:
        count -= 1
        continue
        
    document = Document()
    document.add_paragraph(text_generated)
    document.save(desktop_path + 'word/' + str(count) + '.docx')

driver.quit()
