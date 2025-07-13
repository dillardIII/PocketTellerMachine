# === Adapted for ghostmedic ===
# === FILE: ghost_socks5_scraper.py ===
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

options = Options()
options.headless = True

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "127.0.0.1:9050"
proxy.ssl_proxy = "127.0.0.1:9050"

capabilities = proxy.to_capabilities()

driver = webdriver.Firefox(options=options, desired_capabilities=capabilities)
driver.get("http://check.torproject.org")
print(driver.page_source)
driver.quit()