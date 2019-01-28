Feature: Add new task from mail or message or manually and get its duration
  Adding new tasks

  Scenario: Add new task from the received message
    Given new message or email arrived
     When assistant finds there a task
     Then assistant says "You get message from Alice to do homework at 10.00 at Alice house. Add this task to list?"

  Scenario: Add new task manually
    Given user wants to add task manually
     When user adds task "Do homework as Alice house today at 10.00"
      And assistant processes input
     Then assistant adds new task with proper tags
     Then assistant says "Do you want to know how long this task will take to do?"

  Scenario: User wants to add received task
    Given task exists
      And user wants to add new task from received message
     When user says "Yes"
      And assistant processes input
     Then assistant adds new task with proper tags
      And assistant says "Do you want to know how long this task will take to do?"

  Scenario: User don't want to add new task
    Given task exists
      And user doesn't want to add task
     When user says “No"
      And assistant processes input
     Then assistant exits

  Scenario: User doesn't want to know task duration
    Given task exists
      And user doesn't want to know task duration
     When user says "No"
      And assistant processes input
     Then assistant says "Push start task when you start this task. Push end task when you end it."

  Scenario: User wants to know task duration
    Given task exists
      And user wants to find similar tasks
      And there are similar tasks
     When user says "Yes"
      And assistant processes input
     Then assistant calculates average task duration
      And assistant says "You will need 15 minutes. \nPush start task when you start this task. Push end task when you end it."

  Scenario: User wants to know task duration
    Given task exists
      And user wants to know task duration
      And there are no similar tasks in base
    When user says "Yes"
      And assistant processes input
     Then assistant says "It is the first task of this type, I can't calculate its duration. \nDo you want to find similar tasks in internet?"

  Scenario: User wants to find similar tasks in internet
    Given task exists
      And user wants to find similar tasks
      And there is no internet connection
     When user says "Yes"
      And assistant processes input
     Then assistant says "Can't connect to the internet. Do you want retry?"

  Scenario: User wants to find similar tasks
    Given task exists
      And user wants to find similar tasks
      And there are similar tasks
     When user says "Yes"
      And assistant processes input
     Then assistant calculates average task duration
      And assistant says "You will need 15 minutes. \nPush start task when you start this task. Push end task when you end it."

  Scenario: User wants to find similar tasks in internet
    Given task exists
      And user wants to find similar tasks
      And there are no similar tasks in internet
     When user says "Yes"
      And assistant processes input
     Then assistant says "No similar tasks are found. \nPush start task when you start this task. Push end task when you end it."

  Scenario: User doesn't want to find similar tasks in internet
    Given task exists
      And user doesn't want to find similar tasks
     When user says "No"
      And assistant processes input
     Then assistant says "Push start task when you start this task. Push end task when you end it."

