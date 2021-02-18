from os import path, getcwd
from datetime import date

def get_credentials(manual):
  # Retrieves the absolute path to the credentials file regardless of where the script is being run from
  creds_file_path = getcwd() + "/" + path.dirname(__file__) + "credentials.env"

  if manual and not path.exists(creds_file_path):
    username = input("Enter username (email): ")
    password = input("Enter password: ")
    return username, password
  else:  
    with open(creds_file_path, "r") as env_file:
      return env_file.read().strip().split()

def get_day_name():
  today = date.today()
  today = today.strftime("%d/%m/%Y")
  day, month, year = today.split('/')
  day_name = date(int(year), int(month), int(day))
  return day_name.strftime("%A").strip()

def get_name(manual):
  name_file_path = getcwd() + "/" + path.dirname(__file__) + "name.env"

  if manual and not path.exists(name_file_path):
    return input("Enter name for reservation: ")
  else:
    with open(name_file_path, "r") as env_file:
      return env_file.read().strip()