import os
from flask import Flask
from plexapi.server import PlexServer
import json 
import time


app = Flask(__name__)


plexUrl = os.environ.get('PLEX_SERVER')
plexToken = os.environ.get('PLEX_TOKEN')
plex = PlexServer(plexUrl, plexToken)

@app.route('/')
def hello_world():

    sessions = plex.sessions()
    print(dir(sessions))
    print(dir(sessions[0]))
    text = time.strftime('%A %B, %d %Y %H:%M:%S')
    for session in sessions:
        text += ' ' + str(session.viewOffset) + ' '
    return text