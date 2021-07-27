# HIVE - Human Resource Management Platform.


<img src="static/assets/img/Mock_up.PNG">

## Objective
This Website was created for the purpose of satisfying the criteria for the third Milestone Project (Python and Data Centric Development) as part of Code Institute's Full Stack Software Developer course.
The project features a full-stack website that allows users manage a collective dataset centered around a Human Resource domain. The website was constructed using HTML, CSS, Python, Flask and MongoDB.

## UX & Design

## Strategy

#### Project Goal
The primary goal or 'use case' of the website is to act as a platform where employees and Human Resource professionals of a company can store particular details relating to their employment. Such as, their personal details, contact information. Entitlements such as salary, bonus, position and number of holiday's they have. User's with Administrator level access will be able to assign, edit or remove tasks to employee's based on their email address, they will also be able to set the employees salary, bonus and number of holiday days.
General users can book days off which will be reflected in their total holiday days. they can edit their personal information and mark tasks as complete but they can not edit details about their salary, bonus, position and number of holiday's they have.

#### Ideation
The concept of a HR management platform came from my own experience working in a corporate environment where there was no real way for the HR department to interact with the employee's of the company, other than via email or physically visiting their office. 

#### Site owner goals
Developing this website will and has served as a learning experience. An introduction to using Flask with MongoDB to form my first full-stack website. I want the website to serve as a starting point for me to develop better full-stack websites and applications in the future

#### User goals
To have a collaborative platform where users can maintain personal, employment based data, allocate tasks and entitlements.

#### User Demographics
* HR professionals
* Small-Mid-Large companies
* Company employees

#### User requirements
* Intuitive interface
* Responsive on all form factors
* Easy to use and navigate

#### User Stories
As a general user:
* I would like to be able to register for an account.
* I would like to be able to log in to an existing account.
* I would like to be able to log out of an existing account.
* I would like to edit my personal details.
* I would like to book annual leave days.
* I would like to be able to view tasks assigned to me.
* I would like to be able to mark tasks assigned to me as complete.

As a administrative user:
* I would like to be able to register for an account.
* I would like to be able to log in to an existing account.
* I would like to be able to log out of an existing account.
* I would like to edit my personal details.
* I would like to book annual leave days.
* I would like to be able to view tasks assigned to me.
* I would like to be able to mark tasks assigned to me as complete.
* I would like to assign tasks to general users.
* I would like to edit tasks assigned to general users.
* I would like to edit entitlements of general users based on their position, bonus and salary.

#### Opportunities Matrix

<img src="static/assets/img/opprtunities.PNG">

## Structure

### Current Features
#### Features common to all pages
* Navbar with navigation buttons
* Footer with links to the relevant sections on the info page
* social media icons

#### Landing page features
* A full width page banner descibes exactly what the website is aiming to achieve "Human Resource Management made simple!".
* within the banner there is a call to action for the site visitor to enter their email address to learn more.
* In the main body of the page there are distinct sections that highlight the benefits that HIVE can bring to your organisation.
* At the bottom of the page there is section with user success stories. 
* A further call to action sits under this to once again prompt the visitor to enter their email address.

<img src="static/assets/img/lpf3.PNG">

* If the user is not signed in or not registered, they will see the below navbar button group layout

<img src="static/assets/img/lpf1.PNG">

* If the user is signed in they will see the below button group

<img src="static/assets/img/lpf2.PNG">

#### Registration page features
The registration page features a simple to understand form that collects the majority of the users details that are then displayed on their profile page.
* Importantly there is a switch that changes the type of account between general user and admin level access.
* There is a link at the bottom of the form for the user to navigate to the log in page if they already have an account.
 
<img src="static/assets/img/register.PNG">

#### Log in page features
The Log in page is simple, clean and intuitive.
* The user logs in with their email address and password that were used at registration. 
* If the user does not have an account, there is a link at the bottom of the form for the user to navigate to the registration page.

<img src="static/assets/img/login.PNG">

#### Profile page features
The Profile page contains the richest amount of content and features on the website. 
* The user is greeted with a pleasing layout and personal welcome message, which is slightly different depending if the account is general or admin level. 

<img src="static/assets/img/p1.PNG">

* There is a button for the user to log out of their account safely.
* There is a button for the user to edit their profile details.
* The main body of the profile page contains a variety of personal information about the person.

<img src="static/assets/img/p2.PNG">

* In the current tasks section, active tasks assigned to or by (admin) the user will appear. 
* To view the details of the task the user clicks on the left button describing the task and an accordion drops down.
* Depending on the users access level, they will either see

(general user view)
<img src="static/assets/img/taskopen.PNG">

(admin user view)
<img src="static/assets/img/admintaskopen.PNG">

* The profile page will also display the users Salary, Bonus, Position and Holiday days left. 

<img src="static/assets/img/p4.PNG">

* These details are added by an **admin user only** based on the users email address, via the 'Edit Entitlements' link in the 'Options' dropdown.

<img src="static/assets/img/optionsadmin.PNG">

* Users have the option of booking annual leave days that will be deducted from their total (displayed on their profile). 
* To access this booking from they go via 'Book Annual Leave' in 'Options' same as above.

### Design Features

#### Colours
* The colour pallete of the website is mainly pale greys and blues to give a feeling of calm.
#### Typography
* Use of the Roboto font throughout for a professional look. 
#### Images
* Images included are of a business professional nature. To give a look of collaboration and synergy.  

## Skeleton
### Wireframes
