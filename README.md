# Spotify Playlist Sorter

**A Python script that organizes a Spotify playlist by sorting tracks based on their release dates and creates a new, sorted playlist. Uses the Spotipy library for Spotify API access and OAuth2 for authentication.**

## Features

- Retrieves all tracks from a specified Spotify playlist.
- Sorts the tracks by release date.
- Creates a new playlist with the sorted tracks.
- Avoids duplicate playlist creation by checking existing playlists.

## Requirements

- Python 3.7+
- Spotify Developer Account for API credentials
- A Spotify Premium account (required for full API access)

## Setup

### 1. Clone the Repository

- Run the following commands to clone the repository and navigate to the directory:

``` git clone https://github.com/your-username/spotify-playlist-sorter.git
cd spotify-playlist-sorter
```

### 2. Install Dependencies

- Make sure you have pip installed, then install the required packages:

pip install spotipy python-dotenv

### 3. Set Up Spotify API Credentials

Log in to the SpotifyDeveloperDashboard(https://developer.spotify.com/dashboard/applications) and create a new application.
Note down your **Client ID** and **Client Secret**.
Set the **Redirect URI** to http://localhost:8888/callback (or any other valid URI).
### 4. Configure Environment Variables

- Create a .env file in the root of the project directory and add the following variables:

``` CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
MY_URI=http://localhost:8888/callback
PLAYLIST_ID=your_playlist_id_to_sort
```

- Replace your_spotify_client_id, your_spotify_client_secret, and your_playlist_id_to_sort with the appropriate values.

### 5. Run the Script

- Execute the script:

python main.py

- The script will create a new playlist with tracks from your specified playlist, sorted by their release dates.

## How It Works

**Spotify Authentication**: Authenticates using OAuth2 and accesses the Spotify API with permissions to modify playlists.
**Track Retrieval**: Fetches all tracks in batches (handling pagination for playlists larger than 100 tracks).
**Sorting**: Sorts the tracks by release date.
**Playlist Creation**: Creates a new playlist with a name indicating it's sorted, and adds sorted tracks.
**Duplication Check**: Checks if a sorted playlist already exists to prevent duplicates.
## Example

- If you specify a playlist called "My Favorite Tracks," the script will create a new playlist titled "My Favorite Tracks SORTED" with tracks ordered by release date.

## Troubleshooting

- Ensure your **Client ID**, **Client Secret**, and **Redirect URI** are correct in the .env file.
- Make sure you have a valid Spotify Premium account.
- If you encounter errors related to authentication, delete token.txt (the cached token file) and re-run the script.

## Contributing

- If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

- This project is licensed under the MIT License.

