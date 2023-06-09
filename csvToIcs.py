# File - csvToIcs.py
# My Simple tool to create iCalendar file from given list of events.


import csv
import hashlib

if __name__ == "__main__":
    begin_content = 'BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//hacksw/handcal//NONSGML v1.0//EN\nTZID:Asia/Kolkata\nX-LIC-LOCATION:Asia/Kolkata\n'
    end_content = 'END:VCALENDAR'
    all_events = ''

    with open("./events.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        for row in csvreader:
            if row[0] != 'Subject':
                raw_id = row[1] + row[2]
                event_content = 'BEGIN:VEVENT\n'
                event_content = event_content + 'SUMMARY:' + row[0] + '\n'
                event_content = event_content + 'UID:' + hashlib.md5(raw_id.encode('utf-8')).hexdigest() + '\n'
                event_content = event_content + 'DTSTART;TZID=Asia/Kolkata;VALUE=DATE-TIME:' + row[1] + '\n'
                event_content = event_content + 'DTEND;TZID=Asia/Kolkata;VALUE=DATE-TIME:' + row[2] + '\n'
                if row[3]:
                    event_content = event_content + 'LOCATION:' + row[3] + '\n'
                if row[4]:
                    event_content = event_content + 'DESCRIPTION:' + row[4] + '\n'
                if row[5] == 'Y':
                    event_content = event_content + 'RRULE:FREQ=' + row[6] + '\n'
                if row[7] == 'Y':
                    event_content = event_content + 'BEGIN:VALARM\n'
                    event_content = event_content + 'TRIGGER:' + row[8] + '\n'
                    event_content = event_content + 'ACTION:' + row[9] + '\n'
                    event_content = event_content + 'END:VALARM\n'
                event_content = event_content + 'END:VEVENT\n'
                all_events = all_events + event_content

    text_file = open("events.ics", "wt")
    n = text_file.write(begin_content + all_events + end_content)
    text_file.close()
