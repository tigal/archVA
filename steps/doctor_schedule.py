# from behave import *
from behave import given, when, then


@given('there are doctors in the system')
def given_there_are_doctors(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('there is a polyclinic in the system')
def given_there_in_a_polyclinic(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('doctor is working in the required dates')
def given_doctor_is_working(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('the family member exists in the system')
def given_family_member(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('appointment has been made but not clarified yet')
def given_appointment_made(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('there are family members in the system')
def given_family_member(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('there are some appointments')
def given_there_are_appointments(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('the family base is opened')
def given_family_base_opened(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given('the client knows the pass-code')
def given_client_knows_pass(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@when('the Client says {command}')
def when_client_says_command(context, command):
    input = command.lower()
    context.reply = ""
    if (input == '"show me doctors schedule"'):
        context.reply = "Here's the schedule. Do you wish to make an appointment?"
    elif (input == '"everything is ok"'):
        context.reply = "Done! The appointment is clarified"
    elif (input == '"<something> is wrong. lets remake it"'):
        context.reply = "Current appointment has been deleted"
    elif (input == '"check existing appointments"'):
        context.reply = "Whom of your family do you want to check?"
    elif (input == '"edit the family base"'):
        context.reply = "Please, say the pass-code"

@then("assistant gives the details of the appointment to the client to clarify")
def then_details(context):
    context.reply = "Done! Here are the details. Please, clarify to continue."

@then("assistant opens the base")
def then_opens(context):
    context.reply = "Done! The base is opened. Wish to edit it?"

