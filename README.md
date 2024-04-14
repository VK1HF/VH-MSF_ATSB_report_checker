
On 6th OCT 2023 a man flying plane VH-MSF near Canberra crashed - all occupants died. Pilot and his 3 grandchildren. 

ATSB report URL : https://www.atsb.gov.au/publications/investigation_reports/2023/report/ao-2023-045

As with anything aviation - it takes forever to find out what happened. I wrote this python script to have my rPi run it as a cron job each day to check if the web page has changed - i.e. the final report has been release etc.  If there are changes the script sends a notification via PUSHOVER (https://pushover.net/) .

Use this in your crontab : "0 8 * * * ~/scripts/VH-MSF/vh-msf_checker.py"

This crontab will run the checker at 8am each day. If the day of the week is Monday you should get a pushoever "check_success" notification just so you know it is running ok.

feel free to use or plagiarise the code as much as you like. 
