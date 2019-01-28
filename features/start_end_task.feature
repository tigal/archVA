Feature: start task and measure time

  Scenario: User starts task
    Given user decided to start task
     When user pushes start task "Alice"
     Then timer starts
      And assistant says "Timing of Alice task started..."

  Scenario: User ends task
    Given user started task and wants to stop it
     When user pushes stop task "Alice"
     Then timer stops
      And assistant says "Timing of Alice task ended... \nIt took 3 hours."

  Scenario: User starts task
    Given user decided to start task
     When user pushes start task "Call Floral Shop"
     Then timer starts
      And assistant found floral shop phone number
      And assistant says "Timing of Call Floral Shop task started... \nStart calling +7 812 207-00-07..."

  Scenario: User starts task
    Given user decided to start task
     When user pushes start task "Kite"
     Then timer starts
      And assistant searches for wind conditions
      And assistant says "Timing of Kite task started... \nWind speed is 7m/s. Perfect wind speed for kite"