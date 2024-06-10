import ts3
import os
from dotenv import load_dotenv
from poster import make_a_post

print('Starting...')

DEV = False

# Load environment variables from .env file
load_dotenv()

# Access the variables
TS3_HOST = os.getenv("TS3_HOST") if DEV else os.environ.get("TS3_HOST")
TS3_USERNAME = os.getenv("TS3_USERNAME") if DEV else os.environ.get("TS3_USERNAME")
TS3_PWD = os.getenv("TS3_PWD") if DEV else os.environ.get("TS3_PWD")

# Store client names for disconnect events
client_names = {}  # Dictionary to store names (clid: name)

def bot():
    with ts3.query.TS3Connection(TS3_HOST) as ts3conn:
        ts3conn.login(
            client_login_name=TS3_USERNAME,
            client_login_password=TS3_PWD
        )
        ts3conn.use(sid=1)

        # Register for events
        ts3conn.servernotifyregister(event="server")

        while True:
            event = ts3conn.wait_for_event()

            user_display_name = ''
            joined = False

            reason_id = int(event[0]["reasonid"])

            if reason_id == 0:  # Client connected
                clid = int(event[0]["clid"])
                client_info = ts3conn.clientinfo(clid=clid)
                client_name = client_info[0]["client_nickname"]
                user_display_name = client_name
                joined = True
                client_names[clid] = client_name  # Store the name

            elif reason_id == 8:  # Client disconnected
                clid = int(event[0]["clid"])
                # Retrieve name from the stored dictionary
                client_name = client_names.pop(clid, "Unknown User") 
                user_display_name = client_name
                joined = False

            make_a_post(user_display_name=user_display_name, joined=joined)

def main():
    while True:
        try:
            bot()
        except:
            continue

if __name__ == '__main__':
    main()