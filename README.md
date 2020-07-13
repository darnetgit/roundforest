1. make sure that you have a copy of Python 3.8
2. Download the project code
3. In a terminal window, navigate to the project directory and run 'pip install -r requirements.txt'
4. Set the environment variable FLASK_APP to be application.py. 

On a Mac or on Linux, the command to do this is 'export FLASK_APP=application.py'.\
On Windows, the command is 'set FLASK_APP=application.py'.

5. Run 'flask run' to start up your Flask application

search for an amazon product q&a on http://127.0.0.1:5000 \
get json response at http://127.0.0.1:5000/\<ASIN>/\<page>