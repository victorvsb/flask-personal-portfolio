# Products Registration
## flask-personal-portfolio
Personal portfolio of Flask project

This is a web application that allows one to register products informing its name, branch and price. It's possible to list all products, 
insert new ones, update and delete those already registered.

This project is suposed to have a very simple interface, since it aims to praise the use of Flask framework, implementing its resources.

## Flask resources applied at the project
- Routing URL to functions, without parameters, as well as typed ones;
- Redirection through dynamic built URL;
- Use of different methods (POST, GET);
- Templates with Jinja2;
- Receiving data throug HTML forms;
- Integration of application with SQLite Database (CRUD);

## How to excecute
```
# Clone the repository
git clone https://github.com/victorvsb/flask-personal-portfolio.git

# Get inside the project directory
cd flask-personal-portfolio

# Create the virtual environment
python -m venv venv

# Execute the virtual environment
venv\script\activate

# Install the dependencies
pip install -r requirements

# Create the SQLite database
python database\initial.py

# Execute the project
python app.py
```
