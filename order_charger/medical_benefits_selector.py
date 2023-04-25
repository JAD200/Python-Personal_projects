from selenium.webdriver.common.by import By


def medical_benefits(driver):
    while True:
        benefit_description_value = input("""
Posible selections:
    1: anteojos
    2: anteojos bifocales
    3: lentes de contacto
Input the selected item (or enter 'done' to finish): """).strip().lower()
        if benefit_description_value == 'done' or benefit_description_value == 'listo':
            break

        benefit_description = driver.find_element(
            By.XPATH, "//input[@name='prestacionDescripcion']")
        benefit_description.clear()
        if benefit_description_value == '1':
            benefit_description.send_keys("anteojos")
            benefit_description.find_element(
                By.XPATH, "//div[normalize-space()='Anteojos']").click()
        elif benefit_description_value == '2':
            benefit_description.send_keys("anteojos bifocales")
            benefit_description.find_element(
                By.XPATH, "//div[contains(text(),'Anteojos Bifocales')]").click()
        elif benefit_description_value == '3':
            benefit_description.send_keys("lentes de contacto")
            benefit_description.find_element(
                By.XPATH, "//div[normalize-space()='Lentes de contacto']").click()
        else:
            print(
                f'Error\n{benefit_description_value} is not an possible selection')
            continue

        benefit_quantity_value = input("Input the quantity: ")
        benefit_quantity = driver.find_element(
            By.XPATH, "//input[@name='prestacionCantidad']")
        benefit_quantity.clear()
        benefit_quantity.send_keys(benefit_quantity_value)

        add_benefit_button = driver.find_element(
            By.XPATH, "//button[normalize-space()='Agregar prestación']")
        add_benefit_button.click()
