from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as web_options
from os import path, getcwd

def get_credentials():
  # Retrieves the absolute path to the credentials file regardless of where the script is being run from
  creds_path = getcwd() + "/" + path.dirname(__file__) + "credentials.env"

  with open(creds_path, "r") as env_file:
    return env_file.read().strip().split()

if __name__ == "__main__":
  try:
    # Direct link to the amenities site
    url = "https://www.avalonaccess.com/Information/Information/Amenities"
    
    web_opts = web_options()
    web_opts.set_headless()
    browser = Firefox(options=web_opts)
    
    browser.get(url)

    # login
    username, password = get_credentials()
    
    browser.find_element_by_id("UserName").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("submit-sign-in").click()

    # enter reservation screen
    browser.find_element_by_id("reserve").click()

    print(browser.page_source.encode("utf-8"))

  finally:
    browser.close()
