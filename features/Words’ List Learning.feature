Feature: Words’ List Learning
 Assistant can notify user when user should learn a prepared set of foreign words

 Scenario: Words Adding Intend
   Given user wants to create a set of words
    When user says Add words to learn
    Then assistant says Name the words

    Scenario: Words Adding
   Given user started a request to create a set of words
    When user names the words
    Then assistant says cat dog rat were added
    And assistant asks Do you want to add a title?

  Scenario: Words Adding Fail
   Given user started a request to create a set of words
   When user names the words
   And assistant failed to save a set of words because of recognition error
    Then assistant asks Could you repeat the same set of words?

  Scenario: Unknown Word Disambiguation
   Given assistant hasn’t recognised a word N
    And assistant proposed three similar words
    When user replies which word
    Then assistant adds a selected word to a set

 Scenario: Unknown Word Adding
   Given assistant hasn’t recognised a word N
    And assistant proposed three unsuitable words
    When user adds a word
    Then assistant adds a selected word to a set

  Scenario: Title Adding
   Given assistant proposed to add a title to a set
    And user wants to add a title
    When user adds a title
    Then assistant says The title was saved

  Scenario: Reminder Adding
   Given user wants to set a reminder
    When user adds a reminder
    Then assistant says A reminder is set

  Scenario: Time to Learn
   Given reminder is set
    When it is time to learn
    Then assistant says It’s time to learn the set

  Scenario: Words Learning
   Given it is time to learn a set
    When user agrees
    Then assistant shows a set of words

  Scenario: Stop Learning
   Given user completed learning
    When user says Close a set
    Then assistant closes a set
    And assistant confirms that the task was done

  Scenario: Remove a Reminder
   Given user wants to delete a reminder
    When user says Remove a reminder
    Then assistant removes a reminder
    And assistant confirms that the task was done

  Scenario: Delete a Set
   Given user wants to delete a set
    When user says Delete a set
    Then assistant deletes a set of words
    And assistant confirms that the task was done

  Scenario: Cancel a Task
   Given user wants to cancel a task
    When user says Cancel a task
    Then assistant cancels a current task
    And assistant confirms that the task was done

  Scenario: Postpone a Reminder
    Given user wants to postpone a reminder
    And it is time to learn a set
    When user says Postpone a reminder
    Then assistant postpones a reminder to a selected time
    And assistant confirms that the task was done
