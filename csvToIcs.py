# Script to create iCal file (ics) from a input file.
# This input file should be semicolon separated.


# Sample Input file format :
# Subject;Start Timestamp;End Timestamp;Location;Description
# Really Cool Event;20230530T1000Z;20230530T1100Z;"Mumbai, India";Cool Event
# Awesome event;20230531T1000Z;20230531T1100Z;"Mumbai, India";Excellent Event

import csv
import hashlib

if __name__ == "__main__":
    begin_content = 'BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//hacksw/handcal//NONSGML v1.0//EN\nX-WR-TIMEZONE:Asia/Kolkata\n'
    end_content = 'END:VCALENDAR'
    all_events = ''

    with open("/home/aditya/Documents/events.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        for row in csvreader:
            if row[0] != 'Subject':
                raw_id = row[1] + row[2]
                event_content = 'BEGIN:VEVENT\n'
                event_content = event_content + 'SUMMARY:' + row[0] + '\n'
                event_content = event_content + 'UID:' + hashlib.md5(raw_id.encode('utf-8')).hexdigest() + '\n'
                event_content = event_content + 'DTSTART:' + row[1] + '\n'
                event_content = event_content + 'DTEND:' + row[2] + '\n'
                event_content = event_content + 'LOCATION:' + row[3] + '\n'
                event_content = event_content + 'DESCRIPTION:' + row[4] + '\n'
                event_content = event_content + 'END:VEVENT\n'
                all_events = all_events + event_content

    text_file = open("events.ics", "wt")
    n = text_file.write(begin_content + all_events + end_content)
    text_file.close()
