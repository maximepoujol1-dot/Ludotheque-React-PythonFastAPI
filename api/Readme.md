# Ludotheque-React-PythonFastAPI : API

## Description :

- This FastAPI backend provides endpoints for user authentication, browsing the game catalogue, and managing personal collections.

## Prerequisites:

- we need the lasted version of python and an IDE

## Installation and startup: 

- From the project root, run:

    - py -m pip install -r api/requirements.txt
    - cd api
    - docker compose up -d
    - cd..    
    - py -m api.seed  
    - py -m uvicorn api.main:app --reload 

    - cd web
    - npm install
    - npm run dev

- The backend will be started.  

## Demonstration : 

![Capture du terminal](../user_documentation/screen/terminalDownload.png)

-----

![Capture du terminal](../user_documentation/screen/terminalApi.png)

- You can nown crtl click on "http://127.0.0.1:8000" and acceded to the swagger with "/docs" at the url end.

## Structure :

    api/
    ├── main.py
    ├── seed.py
    ├── requirements.txt
    ├── docker-compose.yml
    ├── .env.example
    ├── core/
    │   ├── config.py
    │   ├── errors.py
    │   └── security.py
    ├── db/
    │   └── session.py
    ├── dependencies/
    │   └── auth.py
    ├── models/
    │   ├── collection.py
    │   ├── item.py
    │   └── user.py
    ├── routers/
    │   ├── auth_routes.py
    │   ├── collection_routes.py
    │   └── items_routes.py
    ├── schemas/
    │   ├── collection.py
    │   ├── items.py
    │   └── user.py
    └── services/
        ├── collection_services.py
        ├── items_services.py
        └── user_service.py

## Contribution :

- Maxime Collette Poujol

## License :

- This project is licensed under the MIT License.

## Additional information:

- this a student project developed within the context of a Ynov project