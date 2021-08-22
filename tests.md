## Testing User Stories

* A = General user
* B = Admin user

### First Impression Case (A,B)

#### Case:
_As a first time user I am looking for information and engagement from the website._
#### Procedure:
* Open browser.
* Navigate to HIVE website.
* On landing page check what options are available on the navbar.
* On landing page scroll down the page to see what information is available.
* On landing page scroll down to the footer and check what information and options are available.
#### Expected outcome:
The user sucessfully obtains the required information to understand what the website is offering.
#### Actual Outcome:
The user sucessfully understands the websites objective and does so by engaging with all aspects of the site.
#### Result:
Pass.

### Test Case 1 (A,B)

#### Case:
_I would like to be able to register for an account._
#### Procedure:
* Open browser.
* Navigate to HIVE website.
* On landing page locate the 'register' button and select.
* Enter user details in registration form.
* Select between general and admin account and submit.
#### Expected outcome:
The user sucessfully registers for an account and their profile is displayed.
#### Actual Outcome:
The user sucessfully registers for an account and their profile is displayed.
#### Result:
Pass.

### Test Case 2 (A,B)

#### Case:
_I would like to be able to log in to an existing account._
#### Procedure:
* Open browser.
* Navigate to HIVE website.
* On landing page locate the 'Log In' button and select.
* Enter user details in log in form.
#### Expected outcome:
The user sucessfully logs in to their account and their profile is displayed.
#### Actual Outcome:
The user sucessfully logs in to their account and their profile is displayed.
#### Result:
Pass.

### Test Case 3 (A,B)

#### Case:
_I would like to be able to log out of an existing account._
#### Procedure:
* On landing page locate the 'Log In' button and select.
* Enter user details and log in to profile page.
* While on profile page locate the 'log out button' on the top left of the screen and select.
#### Expected outcome:
The user sucessfully logs out of their account and session.
#### Actual Outcome:
The user sucessfully logs out of their account and session and flash message confirms.
#### Result:
Pass.

### Test Case 4 (A,B)

#### Case:
_I would like to edit my personal details._
#### Procedure:
* log in to an existing account
* While on profile page locate the 'Edit profile button' on the left of the screen under the welcome message, and select.
* In one or all the input fields, enter a new value and select 'update'.
#### Expected outcome:
The user sucessfully updates their account details.
#### Actual Outcome:
The user sucessfully updates their account details and flash message confirms.
#### Result:
Pass.

### Test Case 5 (A,B)

#### Case:
_I would like to book annual leave days._
#### Procedure:
* log in to an existing account.
* While on profile page locate the 'Options' drop down button on the 'my account' row of the profile page, and select.
* Select 'Book annual leave'.
* From the date picker, select the date range for the number of days you would like to book and select.
#### Expected outcome:
The user sucessfully books (n) number of days off and their new holiday total is displayed on their profile page.
#### Actual Outcome:
The user sucessfully books (n) number of days off, flash message confirms and the new total is reflected on the profile page.
#### Result:
Pass.

### Test Case 6 (A,B)

#### Case:
_I would like to be able to view tasks assigned to me._
#### Procedure:
* log in to an existing account.
* While on profile page scroll down to the bottom of the page under 'current tasks', active tasks will appear (must be assigned by an admin).
* Select the task button to learn more about it.
* If the task is complete the user can select the 'Done' button to remove it from their list of tasks.
#### Expected outcome:
The user sucessfully views and or removes the task displayed on their profile page.
#### Actual Outcome:
The user sucessfully views and or removes the task displayed on their profile page.
#### Result:
Pass.

### Test Case 7 (B)

#### Case:
_I would like to assign tasks to general users._
#### Procedure:
* log in to an existing admin account.
* Navigate to the 'Add Task' button on the navbar.
* Complete task for with relevant details.
* Assign the task to a specific user via their email address in the last input field.
#### Expected outcome:
The task will be created and will appear in the 'current tasks' section of the user who created it and the user who it is assigned to.
#### Actual Outcome:
The task was created successfully and appeared on both profiles of both users.
#### Result:
Pass.

### Test Case 8 (B)

#### Case:
_I would like to edit tasks assigned to general users._
#### Procedure:
* log in to an existing admin account.
* locate the specific task in the 'current tasks' section.
* Select the 'Edit' button.
* Complete the edit of relevant input fields.
* Select the Edit button to save the change.
#### Expected outcome:
The task will be edited and will appear in the 'current tasks' section of the user who created it and the user who it is assigned to.
#### Actual Outcome:
The task was edited successfully and the update appeared on both profiles of each user.
#### Result:
Pass.

### Test Case 9 (B)

#### Case:
_I would like to edit entitlements of general users (or own admin account) based on their position, bonus and salary._
#### Procedure:
* log in to an existing admin account.
* locate the 'Options' drop-down button in the 'my account' section of the users profile page.
* Select the 'Edit entitlement' button.
* Input the email address of the target user.
* Complete the edit of relevant input fields for position, bonus or salary.
* Select the 'update' button to save the edit.
#### Expected outcome:
The employees entitlement will be edited and the information will appear on the right side of their profile page. (must create and log in to the target users account to view)
#### Actual Outcome:
The users entitlements were successfully updated appeared on their profile page.
#### Result:
Pass.

### Test Case 10 - 404 error handling

#### Case:
_I would like to check that if the user navigates to a URL extension that does not exist on my website they will get an appropriate error message and be able to return safely to the homepage_
#### Procedure:
* Navigate to the HIVE website.
* In the browser address bar modify the URL to a page that does not exist e.g. https://hive-human-resources.herokuapp.com/notfound

#### Expected outcome:
The website should return a 404 error page that informs the user that this page does not exist, and also provide navigation back to the homepage.
#### Actual Outcome:
The website returned the appropriate 404 error page with navigation back to the hompage.
#### Result:
Pass.


## Testing Validators

### HTML

https://validator.w3.org/

| Page | errors/warnings | Pass |
|------|-----------------|------|
| index.HTML | None | Yes |
| register.HTML | None | Yes |
| login.HTML | None | Yes |
| info.HTML | None | Yes |
| update_profile.HTML | None | Yes |
| add_task.HTML | None | Yes |
| annual_leave.HTML | None | Yes |
| edit_entitlements.HTML | None | Yes |


### Python

PEP8 Validation.

All linting errors were corrected to be fully PEP8 complient.

A warning rermains in the console "env imported but unused" but these are in fact used, they are just concealed for security.

## Bugs/Issues

Even though I had enabled lower level security Apps to interact with my Google mail account, when I attempted to use an email in the input field I got the following error:
```
534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbts\n5.7.14 y2ku2-8KrWsn_dAUhnkssuTuESwaeG-DNn9hWBpsSpJCmVL ZhH24jzJfd-5bHUdh993dJ7\n5.7.14 a5LsAOJrheyT0cRXIhMSbycqvMAC7sNrizO5qU_6iDescJcQa-QqUUCFVH7IZoWF9uXyrv\n5.7.14 HC9XzAW-pBwgUjV4i_ts8CNhB_yZf2JHOi-wl6gZ9jwAiYLWx DPe7epI> Please log\n5.7.14 in via your web browser and then try again.\n5.7.14 Learn more at\n5.7.14 https://support.google.com/mail/answer/78754 y5sm3059043 9pge.49 - gsmtp
```
The error was appearing every time I attempted to enter an email into the input field that triggers the auto email from flask.

And an email was sent to the email address I used to set up the Flask mail connection.

 _"Sign-in attempt was blocked"_

After some investigation, I found that the following steps needed to be taken:

* Checking allow low secure apps in Google settings (it was already on, tried turing it off and back on)
* Trying the unlock captcha link: https://accounts.google.com/DisplayUnlockCaptcha

This second step worked for me, I:
* Signed out of the Google account associated with the Flask mail function
* Selected the DisplayUnlockCaptcha link
* Signed back into the account
* Re-ran my python script

I then inserted my test email account in the Hive website input field. The auto generated email was sent to this address without issue.

## General Observation

I noticed that in some instances the Heroku App must be given a minute to fire up before registering an account as there can be minor timing issues with the creation of an account. 