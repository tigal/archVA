from behave import given, when, then
from datetime import datetime
from os import path
get_file = lambda f: path.join(path.dirname(path.realpath(__file__)), f.lower() + ".wav")

import module.google_recognition as google_recognition

@given("user wants to create a set of words")
def given_create_words(context):
    context.words = []
    context.action = True

@given("user started a request to create a set of words")
def given_create_words(context):
    context.words = []
    context.action = True

@when("assistant failed to save a set of words because of recognition error")
def given_create_words(context):
    context.words = []

@given("assistant hasn’t recognised a word {N}")
def given_take_word_position(context, N):
    context.word_number = N
    context.words = [] #a mock - should have values from previous scenario

@given("assistant proposed three similar words")
def given_propose_words(context):
    context.suggested_ok = True
    context.suggested_words = []

@given("assistant proposed three unsuitable words")
def given_propose_words(context):
    context.suggested_ok = False

@given("assistant proposed to add a title to a set")
def given_propose_add_title(context):
    context.title = ""
    context.wish_title = False

@given("user wants to add a title")
def given_wish_add_title(context):
    context.wish_title = True
    context.wish_reminder = False
    context.reminder_alarm = False
    context.words = []
    context.request = ''
    context.action = True

@given("user wants to set a reminder")
def given_wish_add_reminder(context):
    context.wish_reminder = True
    context.wish_title = False
    context.reminder_alarm = False
    context.words = []
    context.request = ''
    context.action = True

@given("reminder is set")
def given_reminder_status(context):
    context.reminder_status = True

@given("it is time to learn a set")
def given_reminder_status(context):
    context.reminder_status = True
    context.reminder_alarm = True

@given("user completed learning")
def given_stop_learning(context):
    context.stop_learning = True
    context.action = True

@given("user wants to delete a reminder")
def given_delete_reminder(context):
    context.wish_delete_reminder = True
    context.action = True

@given("user wants to delete a set")
def given_delete_set(context):
    context.wish_delete_set = True
    context.action = True

@given("user wants to cancel a task")
def given_cancel_task(context):
    context.action = False

@given("user wants to postpone a reminder")
def given_postpone_reminder(context):
    context.reminder_time = datetime.now()

@when("user names the words")
def when_user_names_words(context):
    audio_file_name = "play.wav"
    context.words = google_recognition.recognize_file(audio_file_name)
    context.request = ''
    context.wish_title = False
    context.wish_reminder = False
    context.reminder_alarm = False

@when("user says {message}")
def when_user_says_message(context, message):
    context.request = message.lower()
    if not hasattr(context, 'words'):
        context.words = []
    context.wish_title = False
    context.wish_reminder = False
    context.reminder_alarm = False


@when("user agrees")
def when_user_agrees(context):
    context.wish_reminder = False

@when("user repeats the same set of {words}")
def when_user_names_words(context, words):
    context.words = words
    context.request = ''
    context.wish_title = False
    context.wish_reminder = False
    context.reminder_alarm = False

@when("user replies which {word}")
def when_user_resolve_ambiguity(context, word):
    context.word = word

@when("user adds a {word}")
def when_user_adds_word(context, word):
    context.word = word

@when("it is time to learn")
def reminder_alarm(context):
    if context.reminder_status:
        context.reminder_alarm = True
        context.words = []
        context.request = ''
        context.wish_title = False
        context.wish_reminder = False

@then("assistant says {message}")
def assistant_says(context, message):
    if context.request == "add words to learn":
        context.reply = "Name the words"
        # print(context.request + ' ' + context.reply)
    if context.words:
        reply = ""
        for word in context.words:
            reply += word + " "
        reply += "were added"
        context.reply = reply
        # print(context.reply)
    if context.wish_title:
        context.reply = "The title was saved"
        # print(context.reply)
    if context.wish_reminder:
        context.reply = "A reminder is set"
        # print(context.reply)
    if context.reminder_alarm:
        context.reply = "It’s time to learn the set"
        # print(context.reply)
    else:
        print("\nASSISTANT REPLIES: " + context.reply)

@then("assistant asks {message}")
def assistant_asks(context, message):
    context.reply = message
  #  print(context.reply)

@then("assistant adds a selected {word} to a set")
def assistant_adds_word(context, word):
    context.words.append(word)
   # print(context.word)

@then("assistant shows a set of {words}")
def assistant_shows_words(context, words):
    context.words = words

@then("assistant closes a set")
def assistant_closes_set(context):
    context.lesson_stop = True

@then("assistant removes a {reminder}")
def assistant_removes_reminder(context, reminder):
        context.reminder_status = False
 #       print(context.reminder_status)

@then("assistant deletes a set of {words}")
def assistant_deletes_set(context, words):
    context.words = []

@then("assistant cancels a current {task}")
def assistant_cancels_task(context, task):
    context.task = False

@then("assistant postpones a reminder to a selected {time}")
def assistant_postpones_task(context, time):
    context.reminder_time = time

@then("assistant confirms that the task was done")
def assistant_confirms_task(context):
    context.task_confirmed = True
