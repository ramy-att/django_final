# django_final

Created for a final project for a cegep level programming course. 

This website is a blog for soccer lovers where they can post posts about anything football related. The website requires users to register with an optional email, mandatory username, and password before allowing them to post anything; however, they can still view posts if not logged in. The About Football page is a page with general information about the sport, taken from Wikipedia. The about page gives information about the project. To edit their profile users must be logged in and go to the profile page (button located in navigation bar). From there, a user can edit his/her username, profile picture and email. However, for now there is no use for the email and the default profile picture is set when account is created. To create a post the user must be logged in to see a button in the navigation bar that redirects to a page where a post with a title and content can be posted.

This website makes use of Django for backend, html and CSS for markup, sqlite for a database and pillow library to allow uploading images on the website. Code inspired by youtuber Corey Shafer’s Django tutorial playlist (https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p). 
base.html navigation bar taken and edited from https://getbootstrap.com/docs/5.0/components/navbar/
For minor references for css and html:
https://www.w3schools.com/css/default.asp
https://www.w3schools.com/html/default.asp

Sme important notes:

To install Django:
1-	Go to command prompt/terminal and open python then type: pip install Django
2-	Install Django in virtual environment 
3-	In command prompt/terminal type: Django-admin startproject (project name)
•	This creates a directory with the project name that has all necessary files and directories to get started the django project
To run development server and view website:
-	In terminal: python manage.py runserver (where manage.py is the main python file in the project that allows the running of the server)
To install pillow:
-	In terminal open python and type: pip install pillow
Files division:
Main directory ‘django_final’ is the root for ‘blog’, ‘django_final’, ‘media’, and ‘users’
Blog:
•	Focuses on main part of the blog such as creating, editing and deleting posts
-	Migrations: database migrations 
o	A migration is a way to making changes to models, in this case a post
o	In terminal ‘Python manage.py makemigration’  makes migrations based on recent changes
o	In terminal Python manage .py migrate 

To run on local machine: py manage.py runserver

What I learnt:

- Basics of Django (using Models to represent a user's profile, requring login for certain features, purpose of views.py, etc...)
- Basics of HTTP requests
- Basic practice of HTML and Css

What I will improve:

- Add reply feature to blog posts, sending notifcation emails to users that receive a reply 
- Improve HTML and CSS using new skills (currently learning) - simply make the blog page look bettter and make it responsive


