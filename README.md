# Avalon Iron Bot

Python app that automates the process of reserving a gym time slot at [Avalon Bay](https://www.avalonaccess.com/)

This app was created, tested, and used in Spring of 2021. If/when Avalon Bay updates their website there is no gaurantee the app will continue to work.

## Getting started

The first step, as always, is to clone the repo to your machine. Run
```shell
git clone https://github.com/mwcodebase/avalon-iron-bot.git
```

As mentioned, this app is built with Python, so make sure you have [Python3](https://www.python.org/downloads/) installed on your machine.

### Dependencies/Prerequisites

This app has several Python dependencies. Run 
```shell
pip3 install -r requirements.txt
```
in the `/app` directory to install them all.

#### Selenium/geckodriver

This app uses [Selenium](https://selenium-python.readthedocs.io/), and is specifically built to use Firefox as its web browser. After installing the Selenium pip package (above) you will need to install [geckodriver](https://github.com/mozilla/geckodriver).

#### Authenitcation

The app is built to be fully automatic by default, meaning you will have to provide it with your login credentials. You will need to create a `credentials.env` file in the `app` directory. It should contain the following information, verbatim.

`credentials.env`
```text
email_address
password
```

The reservation will be made with the same name that is on the account (which is required by Avalon in the first place).

Notice, the .gitignore file contains `*.env`. While this is not the most elegant solution to avoiding plaintext password leaks, it suffices for a simple app such as this. That being said, if you are uncomfortable having plaintext passwords for whatever reason (potentially a shared machine), then continue reading in the next section for how to run the app manually.

## Using the Avalon Iron Bot

If you are using the default configuration (automatically reserve for 4:00pm same day), you are good to go! Run
```shell
python3 main.py
```
if you are in the repo's `/app` directory, otherwise provide the full path to `main.py` from wherever you are.

This bot is also able to fill out Avalon's COVID-19 Health Screening if you provide the link that is sent to your email. As should be obvious, do not use this bot (or the gym) if you have tested positive for COVID, have interacted with someone who has, or are experiencing symptoms of COVID-19. Be safe, don't spread. When using this bot, the user assumes all liability. Authors of the bot cannot be held responsible.

Finally, consider setting up a [cron job](https://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job) to make the app even more automagical!
`Note: you will have to provide the --skip option when setting up a cron job, otherwise the script will ask for input`

### Running manually

The app can also be run manually. Run
```shell
python3 main.py --manual
```
and the app will print to stdout the time slots available for the current day and allow you to chose which one you want. Also, if the app does not find the `.env` files discussed in [Authentication](#Authenitcation) it will ask you for your username, password, and name. No manual input is stored by the app.

# Contributing

However you like! Reach out, leave comment, open an issue, open a PR, make your own fork; the options under an MIT license are numerous.

Thanks for checking out my project! Now go pick things up and put them down!