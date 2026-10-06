# Ludotheque-React-PythonFastAPI : Web


## Description :

- This section is dedicated to the installation, independent launch, and testing of the web application.

- It allows you to explore and test the different aspects of the frontend independently from the backend and its data.

## Prerequisites:

- The following software is required:

    - Node.js with npm

## Installation and startup: 

- From the project root, run:

    - cd web
    - npm install
    - npm run dev

- The development server will then be started by Vite.

- If you encounter issues with the npm command on Windows, try using npm.cmd instead:

    - npm.cmd install 
    - npm.cmd run dev

## Demonstration :     

![Capture du terminal](../user_documentation/screen/terminalWeb.png)

## Structure :

    web/
    ├── package.json
    ├── package-lock.json
    ├── index.html
    ├── vite.config.ts
    ├── eslint.config.js
    ├── tsconfig.json
    ├── public/
    │   ├── favicon.svg
    │   └── icons.svg
    └── src/
        ├── App.tsx
        ├── App.css
        ├── index.css
        ├── main.tsx
        ├── assets/
        │   ├── font.png
        │   └── hero.png
        ├── components/
        │   ├── Button.tsx
        │   ├── Card.tsx
        │   ├── CatalogueCard.tsx
        │   ├── CatalogueList.tsx
        │   ├── CollectionCard.tsx
        │   ├── CollectionList.tsx
        │   ├── Footer.tsx
        │   ├── Form.tsx
        │   └── Navbar.tsx
        ├── context.tsx/
        │   ├── authContext.tsx
        │   └── collectionContext.tsx
        ├── hooks/
        │   ├── localStorage.ts
        │   └── toggle.ts
        ├── services/
        │   ├── authService.ts
        │   ├── collectionService.ts
        │   ├── httpClient.ts
        │   └── itemService.ts
        ├── types/
        │   ├── api.ts
        │   └── type.ts
        └── view/
            ├── AccountPage.tsx
            ├── CollectionPage.tsx
            ├── HomePage.tsx
            ├── LegalPage.tsx
            ├── LoginPage.tsx
            ├── NotFoundPage.tsx
            └── RegisterPage.tsx

## Contribution :

- Thomas Davrou

- Collette Poujol Maxime

## License :

- This project is licensed under the MIT License.

## Additional information:

- this a student project developed within the context of a Ynov project
