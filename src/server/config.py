from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.getcwd(), "config.env"))

PORT = int(os.environ.get("PORT"))
if not PORT:
    print(Warning("Port is not found int the config Defaulting to the default port."))
    PORT = 6969
