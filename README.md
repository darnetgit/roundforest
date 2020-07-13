a working website is located at https://roundforest.herokuapp.com  
insert a product asin and a page number and the corresponding Q&A from the same amazon page will be displayed.  
for example: https://roundforest.herokuapp.com/B01N3ASPNV/1  

to receive the api JSON response go to https://roundforest.herokuapp.com/v1/:ASIN/:page  
for example: https://roundforest.herokuapp.com/v1/B01N3ASPNV/1

to run manually  
1. make sure that you have a copy of Python 3.8
2. Download the project code
3. In a terminal window, navigate to the project directory and run 'pip install -r requirements.txt'
4. Set the environment variable FLASK_APP to be application.py. 

On a Mac or on Linux, the command to do this is 'export FLASK_APP=application.py'.  
On Windows, the command is 'set FLASK_APP=application.py'.

5. Run 'flask run' to start up your Flask application

search for an amazon product q&a on http://127.0.0.1:5000  
get json response at http://127.0.0.1:5000/v1/:ASIN/:page
