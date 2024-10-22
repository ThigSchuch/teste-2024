License Plate Management System
===============================

# How to run the project
1. Clone the repository
2. You can use `Poetry` or `pip` to install the dependencies
3. Run the project using the command `python manage.py runserver`

# How to run the tests
1. Run the tests using the command `pytest`

# How the project is structured
The project is structured in the following way:
- `base`: Contains the Django settings and the base urls
- `client`: An App that contains the home view, the Client model and its uses
- `utils`: An App contains the utility functions used in the project, such as BaseModel class and base templates
- `vehicle`: An App contains the Vehicle model and its uses