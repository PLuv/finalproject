# Project 3

Web Programming with Python and JavaScript

** Final Project **

This app is meant to track customer and policy data for an insurance agency.

Features:
I tried to use most of the major technology concepts we learned in class.  I did not use socketio, flask, or apis.
The database has a couple accounts, policies, vehicles, coverages, etc. loaded for testing.

to login use:
superuser : phil  pass: abc7777777

regular user: Shelly  pass: abc1234567

**NOTE:** you cannot add users from within the app and must instead do it from admin.  This is purposefull design and not a bug.  Since
users would be employees only the admin would be adding them upon hire.


**NOTE2:** I got my template layout from ProUI then i gutted it to keep only the layout I needed.  This actually ended up probably being a bad
idea because it took me a whole day to customize the layout when I could've just built one from scratch in less time...

**NOTE3:** There are a couple known bugs that I just did not prioritize fixing.
examples: when you change your mind about adding/deleting etc. the javascript code does not clear the forms. Same thing happens with the
content section.  I know this is a simple **form.reset()**  and **.innerHTML = "";** fix but it is 5:00 on due date so i'm out of time.

**Things I learned**
- A lot about Django and using to to make querys and send info back and forth to javascript.
- Django ModelForm and Forms
- Good model construction and model relationships. (i feel like my models is the strong point of my project)
- Planning/future proofing for continued app expansion in regards to model construction.

**Final Note**
I realize i did not incorporate everything into this project.  I spent massive amounts of time on it to get it to where it is today.
I do not know why it took me so long as it seems pretty basic at this point but i had a lot of trouble understanding the query system.
(like 20 hours worth of trouble.  Ridiculous i know)
I did enjoy making the project  Thank you for your time in grading my work this semester.
-Philip