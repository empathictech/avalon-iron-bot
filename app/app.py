from requests import get as get_request
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as web_options
from os import path, getcwd

# creates and populates a Property object from the postings' pages
def collect_info(post, is_test):
  info = post.find("div", class_="info")
  
  # name text formatted as "name \n address"
  name = info.find("div", class_="name").text.strip().split("\n")[0]

  if in_blacklist(name) or in_visited(name, is_test):
    return None

  prop = Property(name)

  # price text formatted as "price \n per X"
  prop.price = " ".join(info.find("div", class_="price").text.strip().split())
  prop.address = info.find("span", class_="address").text.strip()
  prop.availability = info.find("div", class_="search--listing-extras").text.strip()
  prop.link = "https://ochdatabase.umd.edu" + info.find("div", class_="name").find("a")["href"]

  return prop

if __name__ == "__main__":
  # Direct link to the amenities site
  # User is required to login, information is being hidden of course
  url = "https://www.avalonaccess.com/Information/Information/Amenities"
  
  web_opts = web_options()
  web_opts.set_headless()

  browser = Firefox(options=web_opts)
  
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
  
  
  page = get_request(url)
  soup = BeautifulSoup(page.content, "html.parser")
  
  search_results = soup.find(id="expo")
  postings = search_results.find_all("article", class_=compile_regex(r"^ocp-property-search property-\d?.*"))

  parsed_posts = []
  for post in postings:
    prop = collect_info(post, cli_args.test)
    
    if prop is not None:
      parsed_posts.append(prop)

  if not parsed_posts:
    final_message = "No new postings found"
  else:
    if not cli_args.simple:
      gather_commutes(parsed_posts)
    
    final_message = ""
    for prop in parsed_posts:
      final_message += prop.get_info()

  if cli_args.test:
    print(final_message)
  else:
    send_message(final_message)
