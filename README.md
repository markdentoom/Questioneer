## Getting started (backend):

1. Ensure you have python 3.9 installed on your machine
2. Open a terminal and navigate to the main questioneer folder (the one with the readme in it)
3. Create a virtual environment using `python -m venv venv`
4. Activate it using `venv/scripts/activate`
5. Install requirements using `pip install -r requirements.txt`
6. In your terminal navigate to the questioneer/questioneer folder (the one with manage.py in it)
7. Run migrations using `python manage.py migrate`
8. Create a superuser using `python manage.py createsuperuser`
9. Run the backend server using `python manage.py runserver`
10. Click the url in your terminal (should be http://127.0.0.1:8000/) to open the backend of the project in your browser

## Getting started (frontend):

1. Open a terminal and navigate to the questioneer/questioneer/frontend folder
2. Run the frontend server using `npm run serve`
3. Click the url in your terminal (should be http://localhost:8080/) to open the frontend of the project in your browser

## For developers:

- You can sort your python imports using `isort --recursive .`
- Use the `REST Client` vscode extension by Huachao Mao for API testing (as an alternative to Postman)
- I suggest using the `Vetur` vscode extension by Pine Wu for help with Vue development

## Software used

- `Django REST` for the backend
- `VueJS` for the frontend
- `Webpack` for TODO
- `Axios` for network requests
- `REST` Client for API testing
