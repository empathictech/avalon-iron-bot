from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as web_options
from os import path, getcwd

if __name__ == "__main__":
  # Direct link to the amenities site
  url = "https://www.avalonaccess.com/Information/Information/Amenities"
  
  web_opts = web_options()
  web_opts.set_headless()

  browser = Firefox(options=web_opts)
  
  browser.get(url)

  # enter username
  browser.find_element_by_id("map_section_tab").click()

  # enter username
  browser.find_element_by_id("map_section_tab").click()

  browser.close()
