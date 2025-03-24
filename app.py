from flask import Flask, render_template, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from datetime import timedelta
import time
from credentials import COOKIE_KEY, CLIENT_ID, CLIENT_SECRET

app = Flask(__name__)

TOKEN_INFO = 'token_info'

app.secret_key = COOKIE_KEY
app.config['SESSION_COOKIE_NAME'] = 'Cookie'
app.permanent_session_lifetime = timedelta(minutes=5)


def get_token():
    # gets a refreshed token if expired
    token_info = session.get(TOKEN_INFO, None)

    if not token_info:
        raise 'exception'
    
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if (is_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=url_for('redirectPage', _external=True),
        scope='user-read-private user-top-read'
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirectPage')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()


    # Provides access code required to get access_token
    code = request.args.get('code')

    # Gets the access token
    token_info = sp_oauth.get_access_token(code)

    # saves access token in session
    session[TOKEN_INFO] = token_info

    return redirect(url_for('fourweeks', _external = True))

@app.route('/fourweeks')
def fourweeks():
    
    # Checks if access_token is valid
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect(url_for('login', _external=False))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])

    TopArtistAllTime = sp.current_user_top_artists(limit=5, offset=0, time_range='short_term')
    TopSongsAllTime = sp.current_user_top_tracks(limit=3, offset = 0, time_range = 'short_term')
    UserInfo = sp.current_user()

    if os.path.exists(".cache"): 
        os.remove(".cache")

    try:
        return render_template('poster.html', TopArtistAllTime = TopArtistAllTime, TopSongsAllTime = TopSongsAllTime, UserInfo = UserInfo)
    except:
        return render_template('error.html')

@app.route('/sixmonths')
def sixmonths():
    
    # Checks if access_token is valid
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect(url_for('login', _external=False))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])

    TopArtistAllTime = sp.current_user_top_artists(limit=5, offset=0, time_range='medium_term')
    TopSongsAllTime = sp.current_user_top_tracks(limit=3, offset = 0, time_range = 'medium_term')
    UserInfo = sp.current_user()

    if os.path.exists(".cache"): 
        os.remove(".cache")

    try:
        return render_template('poster.html', TopArtistAllTime = TopArtistAllTime, TopSongsAllTime = TopSongsAllTime, UserInfo = UserInfo)
    except:
        return render_template('error.html')


@app.route('/alltime')
def alltime():
        # Checks if access_token is valid
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect(url_for('login', _external=False))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])

    TopArtistAllTime = sp.current_user_top_artists(limit=5, offset=0, time_range='long_term')
    TopSongsAllTime = sp.current_user_top_tracks(limit=3, offset = 0, time_range = 'long_term')
    UserInfo = sp.current_user()

    if os.path.exists(".cache"): 
        os.remove(".cache")

    try:
        return render_template('poster.html', TopArtistAllTime = TopArtistAllTime, TopSongsAllTime = TopSongsAllTime, UserInfo = UserInfo)
    except:
        return render_template('error.html')




if __name__ == "__main__":
    app.run(debug=True)