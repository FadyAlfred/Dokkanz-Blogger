# Dokkanz-Blogger
> THis is advanced version of Galaxy Blogger with the same functionalty but in addtion too 
Real-Time that the user don't have too refresh the page to get the new content just when other 
user create, edit or delte post all other user home page update with new content .

# Install

    1. Install git:  
    `sudo apt-get install -y git`
    2. Clone or download this repo.
    3. Install pip and vitualenv:  
    `sudo apt-get install -y virtualenv`  
    `sudo apt-get install -y python3-pip`
    4. Create a virtual environment:  
    `virtualenv -p python3 ~/.virtualenvs/blogger`
    5. Activate the virtual environment:  
    `source ~/.virtualenvs/dokkanz/bin/activate`
    6. Install requirements in the virtualenv:  
    `pip3 install -r requirements.txt
    7. Activate the virtual environment:  
    `source ~/.virtualenvs/dokkanz/bin/activate`
    8. Make Django database migrations:
    `python manage.py makemigrations`  
    then: `python manage.py migrate`
    9. Create an admin user:  
    `python manage.py createsuperuser`
    10. Run the project locally:  
    `python manage.py runserver`
# Use

      1-Create account if you are new user
      2-Login to your account 
      3-Create post and it will be added to the home page
      4-You can edit/delete your posts in rea-time
      5-You can comment any post even your posts and you can edit/delete comments
