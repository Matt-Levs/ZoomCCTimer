## ZoomCCTimer

A timer app that posts updates of the time as a Closed Caption in a Zoom meeting. This program takes advantage of Zoom's third party closed captioning APIKey to display a timer for all participents in a meeting who enable their closed captioning service.

**Motivation:**
The purpose of this was to create a minimalist timer for any Zoom user without the need for a paid plugin or having the need share their screen that has a timer on it. This program is great for scenarios where a meeting attendee needs to share their screen for a presentation but everyone needs to be aware of the time.

**Build Status:**
Current Features:
- Stopwatch (Count Up) Timer with 'Stop' and 'Reset' functions for local timing
- APIKey testing button to check if the correct URL has been pasted in the entry field
- Time is posted as a Closed Caption every 30 seconds (Hard coded)

Bugs: 
- Timer doesnt run without a valid API key
  - Fails when reaching 30 sec due to fiald POST function
- Start Button doesn't work after Stop is used
  
Future Features:
- Adjustable POST interval (Every 30sec, 1 min, 5 min, 10 min)
- Switch between count-down vs count-up timer
  - Count-down: Set to desired minutes and countdown, send POST when time is reached, continue into "Negative Time" to show overtime amount
- Variable countdown POST interval (every 5min then with 5 min remaining, POST every min, then every 10 sec, then time up)
- Initial screen in window showing instructions for obtaining APIKey 
  - Can also be a simple screen with a URL to the GIThub instructions page
- Future replication of the program onto a webserver
  - Users can either download the program or go to a webpage that has the app

# Development Notes

**Building the App**
This app uses pyinstaller to create a .exe file for the program to run on the users computer. The current build can be found in dist/. To build a new .exe file the command is:

pyinstaller --onefile .\ZoomCCTimer.py


# Resources/References
**Zoom CC API**
https://support.zoom.us/hc/en-us/articles/115002212983-Using-a-third-party-closed-captioning-service

**How to Enable Zoom Closed Captioning in Meetings**
https://support.zoom.us/hc/en-us/articles/4409683389709
