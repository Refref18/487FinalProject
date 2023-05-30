import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Proxy ayarları
proxy_host = '103.174.45.58'  # Proxy sunucusunun IP adresini buraya girin
proxy_port = 8080  # Proxy sunucusunun port numarasını buraya girin

# Chrome seçeneklerini ayarlayın
chrome_options = Options()
chrome_options.add_argument('--headless')  # Başsız (headless) modda çalıştır
chrome_options.add_argument(
    f'--proxy-server=http://{proxy_host}:{proxy_port}')  # Proxy ayarını ekle

# Chrome tarayıcısını başlat
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

# TCP dump komutunu başlat (tarayıcı trafiğini yakalamak için)
#tcpdump_process = subprocess.Popen(['tcpdump', '-i', 'eth0', 'port', str(proxy_port)], stdout=subprocess.PIPE)

# Web sitesine gidin
driver.get('https://chat.openai.com')

"""# İşlemlerin tamamlanmasını bekleyin (bir tuşa basılana kadar)
input('Devam etmek için bir tuşa basın...')

# Bir tuşa basıldığında devam etmek için bekleyin
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.TAG_NAME, 'body'))).click()

# İşlemlerin tamamlanmasını bekleyin (bir tuşa basılana kadar)
input('Devam etmek için bir tuşa basın...')

# Tarayıcıyı kapat
driver.quit()

# TCP dump işlemini sonlandırın
 #tcpdump_process.terminate()"""
