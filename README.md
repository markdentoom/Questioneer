# Questioneer

A reddit-like forum for posting questions built using Django REST and Vue.

## Getting started

1. Create a virtual environment using `python -m venv venv`
2. Activate it using `venv/scripts/activate`
3. In your terminal navigate to the `.../questioneer/questioneer` folder
4. Install backend requirements using `pip install -r requirements.txt`
5. Run migrations using `python manage.py migrate`
6. Run the backend server using `python manage.py runserver`
7. Open a new terminal and navigate to the `.../questioneer/questioneer/frontend` folder
8. Install frontend requirements using `npm i`
9. Run the frontend server using `PS ...\questioneer\questioneer\frontend> npm run serve`
10. Click the url in your terminal (http://127.0.0.1:8000/) to open the project in your browser

## Notable features

### Hot reloading for development
![image](https://user-images.githubusercontent.com/59030690/155032168-f24a5d50-6135-42f4-b68d-1404ba322921.png)

### API testing using `REST Client`
![image](https://user-images.githubusercontent.com/59030690/155032500-4a172b80-a5b2-4e9a-938a-719c612d6078.png)

### Account creation and login
![image](https://user-images.githubusercontent.com/59030690/155032064-f36e7502-2cb2-4ed9-86da-ccdf4db06c2a.png)

### Standard CRUD functionality for questions and answers with authentication and pagination
![image](https://user-images.githubusercontent.com/59030690/155032632-4ef012db-dfa5-40a5-805a-807b3ee038b9.png)

## Built using

- Django REST
- Vue
- Axios
- REST Client

## Contributing

This is a solo project. If you find any issues, please create an issue in the issues tab.
