# Products Registration
## flask-personal-portfolio
Personal portfolio of Flask project

This is a web application that allows one to register products informing its name, branch and price. It's possible to list all products, 
insert new ones, update and delete those already registered.

This project is suposed to have a very simple interface, since it aims to praise the use of Flask framework, implementing its resources.

## Flask resources applied at the project
- Routing URL to functions, without parameters, as well as with typed ones;
- Redirection through dynamic built URL;
- Use of different methods (POST, GET);
- Templates with Jinja2;
- Receiving data throug HTML forms;
- Integration of application with SQLite Database (CRUD);
    - For each table in DataBase, it is suposed to exist one Model class and one DAO class, that together can handle its data, executing all CRUD operation expected in a DataBase System.

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
python data_base\initial.py

# Execute the project
python app.py
```
After installing and executing, as described above, the application will be avaible locally, and can be accessed using a Web Browser through the link http://127.0.0.1:5000
