# iCalendarFileGenerator

Script to create iCal file (ics) from a input file.

The input file should be semicolon separated.
The input file name should be events.csv


Sample Input file format :
```
Subject;Start Timestamp;End Timestamp;Location;Description;Repeat;Freq;Reminder;Trigger;Action
Really Cool Event;20230530T1000Z;20230530T1100Z;"Mumbai, India";Cool Event;Y;YEARLY;Y;-PT1440M;DISPLAY
Awesome event;20230531T1000Z;20230531T1100Z;"Mumbai, India";Excellent Event
```

For repeating events you can set below frequences
1. YEARLY
2. MONTHLY
3. WEEKLY
4. DAILY