import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def start_chrome_app(url):
    options = Options()
    options.add_argument(f"--app={url}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    print("Запуск вашей Discord сессии на движке браузера Chrome...")
    
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        print("Discord успешно запущен..")

        while True:
            if not driver.window_handles:
                break
            time.sleep(0.5)
            
    except Exception as e:
        print("\n[Возникла ошибка]:")
        print(e)
    finally:
        if driver:
            try:
                driver.quit()
                print("Процесс успешно завершен.")
            except:
                pass

if __name__ == "__main__":
    TARGET_URL = "https://discord.com/login" 
    start_chrome_app(TARGET_URL)
    
    print("\nРабота программы завершена.")
    input("Нажмите Enter для выхода...")
