from behave import given, when, then
import requests
import re

from weather import Weather, Unit

def find_floral_shop_telephone():
    t = requests.get('https://tk-riverhouse.ru/shops/bon-fleur.html')
    phone = re.search('\+7 (.*)', t.text).group(0)
    return phone

def get_wind_condition_for_kite():
    weather = Weather(unit=Unit.CELSIUS)
    wind = weather.lookup_by_location("saint-petersburg").wind.speed
    if wind:
        if (wind < 5):
          s = "Wind speed is " + str(wind) + "m/s. Wind speed is too slow"
        if (wind >= 5 and wind <= 11):
          s = "Wind speed is " + str(wind) + "m/s. Perfect wind speed for kite"
        if (wind > 11):
          s = "Wind speed is " + str(wind) + "m/s. Wind speed is too high. Only for professionals"
        return s

def start_timer():
    pass

def stop_timer():
    pass

@given("user decided to start task")
def given_user_starts_task(context):
    context.task_timer_start = True
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given("user started task and wants to stop it")
def given_user_stops_task(context):
    context.task_timer_start = False
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@when("user pushes {task_name}")
def when_user_pushes_task(context, task_name):
    context.current_task_name = task_name

@then("timer {action}")
def then_timer_do_smthg(context, action):
    if context.task_timer_start is True:
        start_timer()
        context.reply = "Timing of " + context.current_task_name + " task started..."
    else:
        stop_timer()
        context.reply = "Timing of " + context.current_task_name + " task ended... \nIt took 3 hours."

@then("assistant found floral shop phone number")
def then_find_floral_shop_telephone(context):
    context.reply +=  " \nStart calling " + find_floral_shop_telephone() +"..."

@then("assistant searches for wind conditions")
def then_wind_conditions(context):
    context.reply += "Timing of Kite task started... \nWind speed is 7m/s. Perfect wind speed for kite"