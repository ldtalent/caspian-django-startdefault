# Starting a Django Project Without the startproject Command

This project demonstrates using Django without the default project setup and also creating projects with a different layout.

## Usage
### Taking it for a spin
- Clone the repository (`git clone https://github.com/learningdollars/caspian-django-startdefault`)
- cd into caspian-django-startdefault
- Install all dependencies (`pip install -r requirements.txt`)
- `python single.py runserver` or `gunicorn single --log-file=-` to run it
### Creating a project using the file as template
- Run `django-admin.py startproject your_project --template=project_name`
Note that: `your_project` should be anything you want to name your project.
- cd into `your_project`
- `python single.py runserver` or `gunicorn single --log-file=-` to run it
