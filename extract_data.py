import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Spotify API Credentials
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    if not client_id or not client_secret:
        return {
            'statusCode': 500,
            'body': json.dumps('Spotify API credentials not found.')
        }
    
    try:
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        # Extract playlist data - Top 200 Global Spotify
        playlist_link = "https://open.spotify.com/playlist/4yNfFAuHcSgzbcSm6q5QDu"
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        
        spotify_data = sp.playlist_tracks(playlist_URI)
        
        # Initialize S3 Client
        s3_client = boto3.client('s3')
        filename = "spotify_raw_" + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".json"
        
        # Save data into S3 bucket
        s3_client.put_object(
            Bucket="wony-spotify-data",
            Key="discover_daily/raw_data/to_process/" + filename,
            Body=json.dumps(spotify_data)
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully uploaded {filename} to S3.')
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
