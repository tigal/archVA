from behave import given, when, then

standard_end = "Push start task when you start this task. Push end task when you end it."

@given("new message or email arrived")
def given_assistant_gets_message(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given("task exists")
def given_task_exists(context):
    pass

@given("user wants to {something}")
def given_user_wants(context, something):
    context.task = something.lower()
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given("user doesn't want to {something}")
def given_user_wants(context, something):
    context.task = something.lower()

@given("assistant ends similar tasks searching")
def given_similar_tasks(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given("assistant tries to connect to the internet")
def given_tries_internet_connection(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False

@given("there is no internet connection")
def given_no_internet_connection(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False
    context.reply = "Can't connect to the internet. Do you want retry?"

@given("there are similar tasks")
def given_there_are_similar_tasks(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False
    context.reply = "You will need 15 minutes. \n" + standard_end

@given("there are no similar tasks in base")
def given_no_tasks_in_base(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False
    context.reply = "It is the first task of this type, I can't calculate its duration. \n" + standard_end

@given("there are no similar tasks in internet")
def given_there_are_no_similar_tasks_in_internet(context):
    context.request = False
    context.words = []
    context.wish_title = ""
    context.wish_reminder = False
    context.reminder_alarm = False
    context.reply = "No similar tasks are found. \n" + standard_end

@when("assistant finds there a task")
def when_task_found(context):
    context.message = "from Alice to do homework at 10.00 at Alice house"
    context.reply = "You get message from Alice to do homework at 10.00 at Alice house. Add this task to list?"

@when('assistant processes input')
def when_ass_process_input(context):
    if context.request == '"yes"':
        if context.task == 'add new task from received message' or context.task == 'add task manually':
          context.reply = "Do you want to know how long this task will take to do?"
    elif context.request == '"no"':
        if context.task == 'know task duration' or "find similar tasks":
            context.reply = standard_end
    else:
        context.reply = "error"

@when("similar tasks are {found} in {where}")
def when_ass_ends_search(context, found, where):
    context.task = "similar tasks are "+found.lower()
    if found.lower() == u'not found':
        if where.lower() == u'base':
            context.reply = "It is the first task of this type, I can't calculate its duration. \nDo you want to find similar tasks in internet?"
        else:
            context.reply = "No similar tasks are found. \n"+standard_end

@when("user adds task {task}")
def when_user_adds_task(context, task):
    context.request = ""
    context.message = task
    context.request = u'"yes"'

@when("internet connection fails")
def when_internet_connection_fails(context):
    context.reply = "Can't connect to the internet. Do you want retry?"

@then("assistant adds new task with proper tags")
def then_add_new_task(context):
    print("\nASSISTANT REPLIES: New task added")

@then('assistant exits')
def then_ass_exits(context):
    print("\nASSISTANT REPLIES: Quiting...")

@then("assistant calculates average task duration")
def then_avg(context):
    context.reply = "You will need 15 minutes. \n"+standard_end