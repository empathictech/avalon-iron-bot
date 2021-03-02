from os import path, getcwd
from datetime import date
from re import compile as compile_regex

def get_credentials(manual):
  # Retrieves the absolute path to the credentials file regardless of where the script is being run from
  creds_file_path = path.dirname(__file__) + "/credentials.env"

  if manual and not path.exists(creds_file_path):
    username = input("Enter username (email): ")
    password = input("Enter password: ")
    return username, password
  else:  
    with open(creds_file_path, "r") as env_file:
      return env_file.read().strip().split()

# A little python magic to get the name of the current day
def get_day_name():
  today = date.today()
  today = today.strftime("%d/%m/%Y")
  day, month, year = today.split('/')
  day_name = date(int(year), int(month), int(day))
  return day_name.strftime("%A").strip()

# Retrieves name and account number from the site header
# This one is kinda strange/very hardcoded as the sites tagging for the elements is... lacking
def get_account_details(driver):
  account_info = driver.find_elements_by_id("dropdown-navigation")[0].text.strip()
  name, account_number = account_info.split("\n")
  account_number = account_number.split("Account: ")[1]
  return name, account_number
