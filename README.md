## Initial setup (backend)

1. Ensure you have python 3.9 installed on your machine
2. Open a terminal and navigate to the `.../questioneer` folder
3. Create a virtual environment using `python -m venv venv`
4. Activate it using `venv/scripts/activate`
5. Install backend requirements using `pip install -r requirements.txt`
6. In your terminal navigate to the `.../questioneer/questioneer` folder
7. Run migrations using `python manage.py migrate`
8. Create a superuser using `python manage.py createsuperuser`
9. In your terminal navigate to the `.../questioneer/questioneer/frontend` folder
10. Install frontend requirements using `npm i`

## Running the project

1. Run the frontend server using `(venv) PS ...\questioneer\questioneer\frontend> npm run serve`
2. In a separate terminal run the backend server using `(venv) PS ...\questioneer\questioneer> python manage.py runserver`
3. Click the url in your terminal (http://127.0.0.1:8000/) to open the project in your browser

## For developers

- This project supports hot reloading
- You can sort your python imports using `isort --recursive .`
- Use the `REST Client` vscode extension by Huachao Mao for API testing (as an alternative to Postman)
- I suggest using the `Vetur` vscode extension by Pine Wu for help with Vue development

## Software used

- `Django REST` for the backend
- `VueJS` for the frontend
- `Webpack` for TODO
- `Axios` for network requests
- `REST` Client for API testing
