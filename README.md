# 🎵 Gramify - Your Spotify Stats in Instagram Style

<div align="center">

[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-v2.0.1-green.svg)](https://flask.palletsprojects.com/)
[![Spotify](https://img.shields.io/badge/spotify-api-1DB954.svg?logo=spotify)](https://developer.spotify.com/documentation/web-api/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

<img src="https://spotify.com/favicon.ico" width="100" height="100" alt="Gramify Logo">

*Transform your Spotify listening history into beautiful Instagram-style posters!* ✨

[Features](#features) • [Setup](#setup) • [Usage](#usage) • [Contributing](#contributing) • [License](#license)

</div>

## ✨ Features

🎨 **Instagram-Style Display**
- View your Spotify stats in a familiar Instagram post layout
- Beautiful, modern UI design inspired by social media
🖼️ **Save & Share**
- Download your stats across multiple time ranges as beautiful images

⏰ **Multiple Time Ranges**
- Last 4 weeks
- Last 6 months
- All time

<p align="center">
  <img src="images/image1.png" width="45%" />

</p>


🎵 **Rich Music Information**
- Top 5 most listened artists
- Top 3 favorite songs
- Interactive links to Spotify

🔒 **Secure & Private**
- Spotify OAuth authentication
- No permanent data storage
- Session-based cookies

📱 **Responsive Design**
- Works seamlessly on desktop and mobile
- Optimized for various screen sizes

## 🚀 Technical Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

</div>

## 🛠️ Setup

### Prerequisites
- Python 3.6 or higher
- Active Spotify account (Free or Premium)
- Spotify Developer account

### Installation Steps

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/gramify.git
cd gramify
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Configure Spotify API**
- Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create a new application
- Set redirect URI: `http://localhost:5000/redirectPage`
- Note your Client ID and Secret

4️⃣ **Set up credentials**
Create `credentials.py` in the root directory:
```python
COOKIE_KEY = 'your_cookie_key'  # Any random string
CLIENT_ID = 'your_client_id'    # From Spotify
CLIENT_SECRET = 'your_client_secret'  # From Spotify
```

5️⃣ **Launch the app**
```bash
python app.py
```

6️⃣ **Access the website**
- Open your browser
- Visit `http://localhost:5000`

## 📱 Usage

1. Click the "Log into Spotify" button
2. Authorize access to your Spotify data
3. View your personalized Instagram-style poster
4. Switch time ranges with the buttons at the top
5. Click any artist or song to open in Spotify




## 🙏 Acknowledgments

- 📸 Inspired by Instagram's beautiful UI design
- 🎵 Powered by Spotify Web API
- 📚 Built with Spotipy library

---
