from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as web_options
from props import Property

# the OCH site has the Google Maps API integrated into it, which is great as it means we don't have to pay for it
def gather_commutes(props_list):
  web_opts = web_options()
  web_opts.set_headless()

  browser = Firefox(options=web_opts)
  
  for prop in props_list:
    browser.get(prop.link)

    # open the map tab
    browser.find_element_by_id("map_section_tab").click()

    # gather walking commute info
    browser.find_element_by_xpath('//*[@title="Walking"]').click()
    
    walk_distance = browser.find_elements_by_class_name("directions--distance")[1].text.strip()
    walk_time = browser.find_elements_by_class_name("directions--time")[1].text.strip()

    # gather bicycle commute info
    browser.find_element_by_xpath('//*[@title="Biking"]').click()

    bike_distance = browser.find_elements_by_class_name("directions--distance")[1].text.strip()
    bike_time = browser.find_elements_by_class_name("directions--time")[1].text.strip()

    prop.commute_info = f"""Walking commute: {walk_distance}, {walk_time}
Biking commute: {bike_distance}, {bike_time}"""

  browser.close()
