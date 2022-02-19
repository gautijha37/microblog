# Microblog
A microblogging web application using Flask and Python. Application is deployed on [Heroku Server](https://microblogging-site.herokuapp.com/index)

# Application
Application python modules are stored in `venv/app/ `.
- forms.py modules interact with web forms using flask_wtf extension and wtforms.
- models.py contain database classes and associated relationships. These classes also contain utility functions for interaction of Users and posts with each other.
- routes.py Contains callback functions for url routes. 

# Templates
HTML templates for application are stored in `venv/app/templates/`.
- 404.html : Error page.
- 505.html : Error page.
- \_post.html : Template for a single post
- base.html : Base application template
- edit_profile.html : Editing the about or username of a user
- index.html : Home page
- login.html : Renders the sign in form
- register.html : Form to take details of a new user and add it to database.
- user.html : Home page for a user - displays posts of the own user and those followed by the user.
