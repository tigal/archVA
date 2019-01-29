Feature: Family Doctors' Schedule Manager

  Scenario: Checking the doctors' working schedule
     Given there are doctors in the system
       And there is a polyclinic in the system
      When the Client says "Show me doctors schedule"
      Then assistant says "Here's the schedule. Do you wish to make an appointment?"

  Scenario: Making an appointment with the exact doctor
     Given doctor is working in the required dates
       And the family member exists in the system
      When the Client says "Make an appointment for <family member's name>"
      Then assistant gives the details of the appointment to the client to clarify
       And assistant says "Done! Here are the details of the appoirtment. Please, clarify to continue."

  Scenario: Appointment clarification
      Given appointment has been made but not clarified yet
       When the Client says "Everything is OK"
       Then assistant says "Done! The appointment is clarified"

  Scenario: Appointment cancellation
     Given appointment has been made but not clarified yet
      When the Client says "<something> is wrong. Lets remake it"
      Then assistant says "Current appointment has been deleted"

  Scenario: Checking appointments that are on agenda
     Given there are family members in the system
       And there are some appointments
      When the Client says "Check existing appointments"
      Then assistant says "Whom of your family do you want to check?"

  Scenario: Family base opening
     Given there are family members in the system
      When the Client says "Open the family base"
      Then assistant opens the base
       And assistant says "Done! The base is opened. Wish to edit it?"

  Scenario: Family base editing request processing
     Given the family base is opened
       And the client knows the pass-code
      When the Client says "Edit the family base"
      Then assistant says "Please, say the pass-code"