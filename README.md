# IPAM 
## This project was done according to:
[Integrate IPAM in an existing Django project](https://github.com/openwisp/openwisp-ipam#setup-integrate-in-an-existing-django-project)

### Installation steps
1. ```git clone git@github.com:DavidMeu/ipam_poc.git```
2. ```pip install -r requirements```
3. ```./manage.py migrate``` (Synchronizes the database state with the current set of models and migrations)
4. ```./manage.py createsuperuser``` (create a user who can login to the admin site for example username: ipam, password:123)
5. ```./manage.py runserver``` (Starts a lightweight development Web server on the local machine)
6. Create a token for that user to interact with the IPAM service. (you can do it via the admin site http://127.0.0.1:8000/admin)
