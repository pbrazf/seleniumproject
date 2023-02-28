# erros: quebra captcha e data

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# 1:
driver = webdriver.Chrome()  # definindo chrome como navegador
driver.get('https://www.tjsp.jus.br/cac/scp/pesquisainternetpagamento.aspx')  # chegando ao site
sleep(1)

''' 
# 3:
# encontrando caixa pelo id e clicando
driver.find_element('id', 'vTIPONOME1').click()
if autoradvogado == '2':
    driver.find_element('id', 'vTIPONOME2').click()
sleep(1)
# encontrando caixas pelo id e preenchendo
driver.find_element('id', 'vNOME').send_keys('Maria Celeste Dalanesi Rosa')
sleep(1)
driver.find_element('id', 'vCRE_CPF_CNPJ').send_keys('14952130800')
sleep(1)

# ++++++ ERRO DATA
 data = driver.find_element(By.XPATH, '//*[@id="vCRE_DT_NASCIMENTO"]')
driver.switch_to.frame(data)
driver.switch_to.default_content()
data.send_keys('09112005') 

date_element = driver.find_element('id', 'vCRE_DT_NASCIMENTO')
driver.find_element(By.ID, 'TEXTBLOCK11').click()
date_element.click()
date_element.send_keys('09/11/2005')
sleep(1)
'''

# 2:
driver.get("https://www.tjsp.jus.br/cac/scp/pesquisainternetpagamento.aspx")
driver.find_element(By.ID, "vTIPONOME1").click()
driver.find_element(By.ID, "vNOME").click()
driver.find_element(By.ID, "vNOME").send_keys("Maria Celeste Dalanesi Rosa")
driver.find_element(By.ID, "vCRE_CPF_CNPJ").click()
driver.find_element(By.ID, "vCRE_CPF_CNPJ").send_keys("14952130800")

driver.execute_script("document.getElementById('vCRE_DT_NASCIMENTO').setAttribute('value','16/09/1943')")

# 3:
# quebrando captcha
link_imagem = driver.find_element(By.XPATH, '//*[@id="captchaImage"]/img')
imagem = link_imagem.get_attribute('src')  # conseguindo current source das imagens
r = 0

if imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/1.jpg':
    r = 'polish'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/2.jpg':
    r = 'soap'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/3.jpg':
    r = 'wood'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/4.jpg':
    r = 'great'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/5.jpg':
    r = 'school'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/6.jpg':
    r = 'sudden'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/7.jpg':
    r = 'wind'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/8.jpg':
    r = 'step'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/9.jpg':
    r = 'credit'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/10.jpg':
    r = 'pain'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/11.jpg':
    r = 'design'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/12.jpg':
    r = 'front'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/13.jpg':
    r = 'profit'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/14.jpg':
    r = 'push'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/15.jpg':
    r = 'seem'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/16.jpg':
    r = 'cord'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/17.jpg':
    r = 'sound'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/18.jpg':
    r = 'scale'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/19.jpg':
    r = 'with'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/20.jpg':
    r = 'wind'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/21.jpg':
    r = 'cloth'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/22.jpg':
    r = 'screw'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/23.jpg':
    r = 'garden'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/24.jpg':
    r = 'bent'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/25.jpg':
    r = 'west'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/26.jpg':
    r = 'judge'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/27.jpg':
    r = 'goat'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/28.jpg':
    r = 'animal'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/29.jpg':
    r = 'warm'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/30.jpg':
    r = 'join'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/31.jpg':
    r = 'turn'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/32.jpg':
    r = 'school'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/33.jpg':
    r = 'white'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/34.jpg':
    r = 'keep'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/35.jpg':
    r = 'collar'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/36.jpg':
    r = 'basin'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/37.jpg':
    r = 'tooth'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/38.jpg':
    r = 'face'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/39.jpg':
    r = 'range'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/40.jpg':
    r = 'tight'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/41.jpg':
    r = 'nail'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/42.jpg':
    r = 'seem'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/43.jpg':
    r = 'female'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/44.jpg':
    r = 'public'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/45.jpg':
    r = 'potato'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/46.jpg':
    r = 'where'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/47.jpg':
    r = 'idea'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/48.jpg':
    r = 'snake'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/49.jpg':
    r = 'flower'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/50.jpg':
    r = 'narrow'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/51.jpg':
    r = 'still'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/52.jpg':
    r = 'hope'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/53.jpg':
    r = 'glass'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/54.jpg':
    r = 'lock'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/55.jpg':
    r = 'hand'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/56.jpg':
    r = 'face'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/57.jpg':
    r = 'weight'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/58.jpg':
    r = 'fear'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/59.jpg':
    r = 'copper'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/60.jpg':
    r = 'debt'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/61.jpg':
    r = 'shoe'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/62.jpg':
    r = 'paint'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/63.jpg':
    r = 'butter'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/64.jpg':
    r = 'roll'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/65.jpg':
    r = 'blood'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/66.jpg':
    r = 'story'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/67.jpg':
    r = 'doubt'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/68.jpg':
    r = 'again'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/69.jpg':
    r = 'meat'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/70.jpg':
    r = 'offer'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/71.jpg':
    r = 'clean'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/72.jpg':
    r = 'memory'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/73.jpg':
    r = 'like'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/74.jpg':
    r = 'wrong'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/75.jpg':
    r = 'jump'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/76.jpg':
    r = 'amount'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/77.jpg':
    r = 'regret'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/78.jpg':
    r = 'free'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/79.jpg':
    r = 'weight'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/80.jpg':
    r = 'crush'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/81.jpg':
    r = 'pull'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/82.jpg':
    r = 'dress'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/83.jpg':
    r = 'door'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/84.jpg':
    r = 'male'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/85.jpg':
    r = 'black'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/86.jpg':
    r = 'please'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/87.jpg':
    r = 'flag'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/88.jpg':
    r = 'fact'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/89.jpg':
    r = 'nose'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/90.jpg':
    r = 'boat'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/91.jpg':
    r = 'taste'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/92.jpg':
    r = 'snake'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/93.jpg':
    r = 'cold'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/94.jpg':
    r = 'attack'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/95.jpg':
    r = 'crush'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/96.jpg':
    r = 'canvas'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/97.jpg':
    r = 'shame'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/98.jpg':
    r = 'book'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/99.jpg':
    r = 'wound'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/100.jpg':
    r = 'nation'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/101.jpg':
    r = 'small'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/102.jpg':
    r = 'fire'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/103.jpg':
    r = 'good'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/104.jpg':
    r = 'past'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/105.jpg':
    r = 'profit'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/106.jpg':
    r = 'sound'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/107.jpg':
    r = 'chin'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/108.jpg':
    r = 'flag'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/109.jpg':
    r = 'body'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/110.jpg':
    r = 'salt'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/111.jpg':
    r = 'birth'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/112.jpg':
    r = 'crime'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/113.jpg':
    r = 'erro'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/114.jpg':
    r = 'sleep'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/115.jpg':
    r = 'part'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/116.jpg':
    r = 'square'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/117.jpg':
    r = 'canvas'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/118.jpg':
    r = 'mine'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/119.jpg':
    r = 'safe'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/120.jpg':
    r = 'mark'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/121.jpg':
    r = 'degree'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/122.jpg':
    r = 'bell'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/123.jpg':
    r = 'color'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/124.jpg':
    r = 'expert'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/125.jpg':
    r = 'rule'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/126.jpg':
    r = 'when'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/127.jpg':
    r = 'parcel'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/128.jpg':
    r = 'degree'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/129.jpg':
    r = 'waste'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/130.jpg':
    r = 'after'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/131.jpg':
    r = 'army'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/132.jpg':
    r = 'moon'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/133.jpg':
    r = 'brain'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/134.jpg':
    r = 'news'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/135.jpg':
    r = 'silver'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/136.jpg':
    r = 'rain'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/137.jpg':
    r = 'much'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/138.jpg':
    r = 'stiff'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/139.jpg':
    r = 'horse'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/140.jpg':
    r = 'smile'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/141.jpg':
    r = 'shirt'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/142.jpg':
    r = 'this'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/143.jpg':
    r = 'grip'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/144.jpg':
    r = 'sharp'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/145.jpg':
    r = 'knot'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/146.jpg':
    r = 'neck'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/147.jpg':
    r = 'woman'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/148.jpg':
    r = 'seed'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/149.jpg':
    r = 'smell'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/150.jpg':
    r = 'round'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/151.jpg':
    r = 'linen'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/152.jpg':
    r = 'same'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/153.jpg':
    r = 'right'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/154.jpg':
    r = 'adjust'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/155.jpg':
    r = 'jewel'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/156.jpg':
    r = 'bell'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/157.jpg':
    r = 'pocket'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/158.jpg':
    r = 'green'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/159.jpg':
    r = 'soap'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/160.jpg':
    r = 'mother'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/161.jpg':
    r = 'mine'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/162.jpg':
    r = 'rice'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/163.jpg':
    r = 'lost'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/164.jpg':
    r = 'tail'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/165.jpg':
    r = 'foot'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/166.jpg':
    r = 'porter'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/167.jpg':
    r = 'spring'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/168.jpg':
    r = 'desire'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/169.jpg':
    r = 'screw'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/170.jpg':
    r = 'glove'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/171.jpg':
    r = 'spade'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/172.jpg':
    r = 'bent'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/173.jpg':
    r = 'letter'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/174.jpg':
    r = 'glass'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/175.jpg':
    r = 'sugar'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/176.jpg':
    r = 'fear'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/177.jpg':
    r = 'every'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/178.jpg':
    r = 'muscle'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/179.jpg':
    r = 'right'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/180.jpg':
    r = 'rate'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/181.jpg':
    r = 'sticky'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/182.jpg':
    r = 'butter'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/183.jpg':
    r = 'sail'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/184.jpg':
    r = 'summer'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/185.jpg':
    r = 'snake'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/186.jpg':
    r = 'whell'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/187.jpg':
    r = 'sheep'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/188.jpg':
    r = 'gloove'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/189.jpg':
    r = 'poison'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/190.jpg':
    r = 'tooth'
elif imagem == 'https://www.tjsp.jus.br/cac/scp/Captcha/images/191.jpg':
    r = 'bucket'

driver.find_element('id', '_cfield').send_keys(r)
sleep(1)

# 4:
# passando a proxima pagina
# WebDriverWait(driver, timeout=5).until(driver.find_element('name', 'BUTTON3').click())
driver.find_element('name', 'BUTTON3').click()
sleep(6)

# 5:
# fazendo download do arquivo
driver.find_element('id', 'vSELECIONAR_0004').click()
sleep(3)



