## Initial Commit - Basic User Login:
1. pip install flask
2. pip install flask-wtf
3. Creating the Jinja2 template
4. pip install flask-sqlalchemy
5. pip install flask-migrate
6. Optional: Set SQLAlchemy database Uri to PostgreSQL
6. Creating, connecting and migrating database to the web application
7. pip install flask-login
8. Creating user logins
9. Snapshot --> local repo --> Github


## Second Commit - User Profile
1. Creating user profile page
2. Snapshot --> local repo --> Github


## Third Commit - Error Handling
1. Creating error template 
2. Setting up database session rollback for error 500
3. Setting up email and file logging
4. Adding validate_username in EditProfileForm class to avoid duplicate username
5. Snapshot --> Local repo --> Github


## 4th Commit - Followers, Posts and Pagination
1. Create Followers table and update User model.
2. Update view to implement posts and pagination
3. Snapshot --> Local repo --> Github


## 5th Commit - Email Support
1. Set reset password using token from pyjwt
2. Create email automation to send the reset password link
3. Snapshot --> Local repo --> Github