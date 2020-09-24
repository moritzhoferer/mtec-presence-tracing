#! /usr/bin/python3

import os
import sys
import pandas as pd
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

script_dir = os.path.dirname(os.path.realpath(__file__))
user_data_path = script_dir + '/user_data.csv'

building_list = ['LEE', 'SEC', 'SOL', 'WEV', 'ZUE']
id_prefix = '_content_specialinterest_mtec_d-mtec_en_news_corona_coronavirus-tracking---attendance-at-d-mtec-facilities_jcr_content_par_container_'


def open_firefox(headless=True) -> webdriver.firefox.webdriver.WebDriver:
    print('Opening Firefox...')
    from selenium.webdriver.firefox.options import Options
    _driver_options = Options()
    if headless:
        _driver_options.add_argument('-headless')
    return webdriver.Firefox(executable_path='geckodriver', options=_driver_options)
    

# def open_chrome(headless=True):
#     print('Opening Chrome...')
#     from selenium.webdriver.chrome.options import Options
#     _driver_options = Options()
#     if headless:
#         _driver_options.add_argument('-headless')
#     return webdriver.Chrome(executable_path='chromedriver', options=_driver_options)


def load_user_data() -> dict:
    _dict = pd.read_csv(
        './user_data.csv',
        header=None,
        index_col=0,
        squeeze=True,
    ).to_dict()
    return _dict


def setup() -> None:
    import inquirer
    
    if os.path.exists(user_data_path):
        user_data = load_user_data()
        questions = [
            inquirer.Text(
                'first_name',
                message='Enter first name',
                default=user_data['first_name'],
            ),
            inquirer.Text(
                'last_name',
                message='Enter last name',
                default=user_data['last_name'],
            ),
            inquirer.Text(
                'mail_address',
                message='Enter e-mail address',
                default=user_data['mail_address'],
            ),
            inquirer.List(
                'building',
                message="Which building are you in?",
                choices=building_list,
                default=user_data['building']
            ),
            inquirer.Text(
                'floor',
                message='Enter floor',
                default=user_data['floor']
            ),
            inquirer.Text(
                'room',
                message='Enter room number',
                default=user_data['room'],
            ),
            inquirer.Confirm(
                'receive_copy',
                message='Do you want to receive a copy via email?',
                default=user_data=='False',

            ),
        ]
    else:
        questions = [
            inquirer.Text(
                'first_name',
                message='Enter first name',
            ),
            inquirer.Text(
                'last_name',
                message='Enter last name',
            ),
            inquirer.Text(
                'mail_address',
                message='Enter e-mail address',
            ),
            inquirer.List(
                'building',
                message="Which building are you in?",
                choices=building_list,
            ),
            inquirer.Text(
                'floor',
                message='Enter floor',
            ),
            inquirer.Text(
                'room',
                message='Enter room number',
            ),
            inquirer.Confirm(
                'receive_copy',
                message='Do you want to receive a copy via email?',
                default=True,

            ),
        ]
    user_data = inquirer.prompt(questions)
    pd.Series(user_data).to_csv(user_data_path)
    print('Successfully saved user data.')

def main() -> None:
    if not os.path.exists(user_data_path):
        setup()

    user_data = load_user_data()

    presence_date = date.today().strftime("%d.%m.%Y")
    arrival_time = sys.argv[1][0:2] + ':' + sys.argv[1][2:4]
    departure_time = sys.argv[2][0:2] + ':' + sys.argv[2][2:4]
    
    driver = open_firefox(headless=True)
    driver.get('https://mtec.ethz.ch/news/corona/contact-tracing.html')

    first_name_box = driver.find_element_by_id(id_prefix + 'first')
    first_name_box.send_keys(user_data['first_name'])

    last_name_box = driver.find_element_by_id(id_prefix + 'last')
    last_name_box.send_keys(user_data['last_name'])

    mail_address_box = driver.find_element_by_id(id_prefix + 'email')
    mail_address_box.send_keys(user_data['mail_address'])

    presence_date_box = driver.find_element_by_id(id_prefix + 'date')

    presence_date_box.send_keys(presence_date)

    arrival_time_box = driver.find_element_by_id(id_prefix + 'arrival')
    arrival_time_box.clear()
    arrival_time_box.send_keys(arrival_time)

    departure_time_box = driver.find_element_by_id(id_prefix + 'departure')
    departure_time_box.clear()
    departure_time_box.send_keys(departure_time)

    building_box = driver.find_element_by_id(id_prefix + 'building')
    building_box.send_keys(user_data['building'])

    floor_box = driver.find_element_by_id(id_prefix + 'floor')
    floor_box.send_keys(user_data['floor'])

    room_box = driver.find_element_by_id(id_prefix + 'room')
    room_box.send_keys(user_data['room'])

    if user_data['receive_copy']=='True':
        check_box = driver.find_element_by_id(id_prefix + 'userMailCheck')
        check_box.click()
        copy_mail_box = driver.find_element_by_id(id_prefix + 'userMailField')
        copy_mail_box.send_keys(user_data['mail_address'])

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    wait_slow = WebDriverWait(driver, 60, poll_frequency=.1)
    finish_button = wait_slow.until(
        ec.element_to_be_clickable((By.NAME, 'formFinish')))
    finish_button.click()
    
    driver.quit()   


if __name__ == '__main__':
    main()
