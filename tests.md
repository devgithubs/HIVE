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

## Testing Validators
## Testing Features
