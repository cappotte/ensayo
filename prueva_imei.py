
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el controlador de Selenium
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Abre la página de verificación de IMEI
driver.get('https://www.imeicolombia.com.co/')

# Espera a que se cargue la página
time.sleep(5)

# Encuentra el campo de entrada para el IMEI y el botón de envío
imei_input = driver.find_element(By.NAME, 'imei')  # Ajusta el selector según sea necesario
submit_button = driver.find_element(By.NAME, 'submit')  # Ajusta el selector según sea necesario

# Ingresa el IMEI
imei_input.send_keys('123456789012345')  # Reemplaza con el IMEI que deseas verificar

# Envía el formulario
submit_button.click()

# Espera a que se cargue la página de resultados
time.sleep(5)

# Extrae los resultados
result = driver.find_element(By.ID, 'result')  # Ajusta el selector según sea necesario
print(result.text)

# Cierra el navegador
driver.quit()