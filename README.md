# Avalon Iron Bot

Python app that automates the process of reserving a gym time slot at https://www.avalonaccess.com/ (Avalon Bay Communities resident portal).

This app was created, tested, and used in Spring of 2021. If/when Avalon Bay updates their website(s) there is no gaurantee the app will continue to work.

## Getting started

The first step, as always, is to clone the repo to your machine. Run
```shell
git clone https://github.com/mwcodebase/och-watchdog.git
```

As mentioned, this app is built with Python, so make sure you have Python3 (any sub-version) installed on your machine: https://www.python.org/

### Dependencies/Prerequisites

This app has several Python dependencies. Run 
```shell
pip3 install -r requirements.txt
```
in the `/app` directory to install them all.

#### Selenium/geckodriver

This app uses Selenium, and is specifically built to use Firefox as its web browser. After installing the Selenium pip package (above) you will need to install geckodriver. Download the latest release here: https://github.com/mozilla/geckodriver/releases At the time of writing, geckodriver has versions for Linux, MacOS, and Windows. Linked below are docs for Selenium and geckodriver if you would like to learn more.

https://selenium-python.readthedocs.io/
https://github.com/mozilla/geckodriver

Detail the steps required to be able to use the project here.

#### Authenitcation

The app is built to be fully automatic by default, meaning you will have to provide it with your login credentials and the name of whoever is reserving the gym. You will need to create `credentials.env` and `name.env` files in the `app` directory. They should contain the following information, verbatim.

`credentials.env`
```text
email_address
password
```

`name.env`
```text
John Doe
```

Notice, the .gitignore file contains `*.env`. While this is not the most elegant solution to avoiding plaintext password leaks, it suffices for a simple app such as this. That being said, if you are uncomfortable having plaintext passwords for whatever reason (potentially a shared machine), then continue reading in the next section for how to run the app manually.

## Using the Avalon Iron Bot

If you are using the default configuration (automatically reserve for 4:00pm same day), you are good to go! Run
```shell
python3 app.py
```
if you are in the repo's `/app` directory, otherwise provide the full path to `app.py` from wherever you are.

Also, consider setting up a cron job for the app for even more automagic: https://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job

### Running manually

The app can also be run manually. Run
```shell
python3 app.py --manual
```
and the app will print to stdout the time slots available for the current day and allow you to chose which one you want. Also, if the app does not find the `.env` files discussed in [Authentication](#Authenitcation) it will ask you for your username, password, and name. No manual input is stored by the app.

## FAQ

If you have any questions or issues, you might find a solution in the [FAQ](FAQ.md)

## Contributing

If you would like to contribute to {PROJECT_NAME}, please see how in [CONTRIBUTING](CONTRIBUTING.md)

## License

This project is licensed under the terms of the [MIT license](LICENSE.txt).

## Thank you

Thanks for checking out my project! Now go pick things up and put them down!