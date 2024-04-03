# <img src="public/logo.png" alt="image" width="36"> InfoSphere

## Project Setup

### Python environment

#### Ubuntu and MaxOS

- Install virtualenv package `sudo apt-get install -y python3-venv`.
- Setup venv by: `python3 -m venv .venv`
- Activate the env by: `source .venv/bin/activate`

#### Windows

- The venv package comes inbuilt with the python package.
- Setup venv by: `python -m venv .venv`
- Activate the env by: `.venv\Scripts\activate`

Install the required packages by: `pip install -r requirements.txt`

#### Ubuntu and MaxOS

- Run the backend server by `python3 -m src.server`

#### Windows

- Run the backend server by `python -m src.server`

**Please wait for the server complete loading the assets**

### Node.js Setup

- Install the npm packages by `npm i`
- Run the client/frontend by `npm run dev`

Once both the client and the server are running you can use the app.
