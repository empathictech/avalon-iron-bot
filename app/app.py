from bs4 import BeautifulSoup
from requests import get as get_request
from argparse import ArgumentParser
from re import compile as compile_regex
from props import Property
from selenium_driver import gather_commutes
from smtp_driver import send_message
from os import path, getcwd

# checks if a property has been visited yet, if not add it to the file
def in_visited(property_name, is_test):
  visited_path = getcwd() + "/" + path.dirname(__file__) + "/visited.env"
  
  with open(visited_path, "r") as visited:
    if property_name in visited.read():
      return True

    if not is_test:
      with open(visited_path, "a") as visited:
        visited.write(f"{property_name}\n")

  return False

# checks the current posting against a blacklist of property managers that are dorm-style
# there is of course the chance of blacklisting posts that mention these buildings, but it is a worthy risk
def in_blacklist(property_name):
  black_list = ["UNIVERSITY VIEW", "COMMONS", "COURTYARDS", "LANDMARK", "TERRAPIN ROW", "VARSITY"]
  
  if any([org in property_name.upper() for org in black_list]):
    return True
  else:
    return False

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
  cli_parser = ArgumentParser()

  cli_parser.add_argument("--test", "-t", help="Send results to stdout", action="store_true")
  cli_parser.add_argument("--simple", "-s", help="Do not gather commute info", action="store_true")

  cli_args = cli_parser.parse_args()

  # sadly, https://ochdatabase.umd.edu/, doesn't have an API, but there is a degree of consistency to search queries and their matching URLs
  # the simplest way forward is to build a search manually and then copy/paste the URL below, as we have done
  url = "https://ochdatabase.umd.edu/housing/price-under+2100"
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
