import json
import usrDetails
import requests

class Playlist:

    def __init__(self):
        self.userId = usrDetails.spotifyUserId
        self.spotifyToken = usrDetails.spotifyToken


    # Log in Youtube
    def getYouTubeClient(self):
        pass


    # Get all the relevant videos
    def getLikedVideos(self):
        pass


    # Create new playlist in Spotify
    def createPlaylist(self):
        requestBody = json.dumps({
            "name": "Imported YouTube Playlist",
            "description": "Imported automatically by Yonatan Kalma",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(usrDetails.spotifyToken)
        response = requests.post(
            query,
            data=requestBody,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(usrDetails.spotifyToken)
            }
        )
        responseJson = response.json()

        # Playlist id:
        return responseJson["id"]



    # Search for video
    def getSpotifyUri(self, songName, artist):

        query = 1


    # Add the song to the playlist
    def addSongToPlaylist(self):
        pass




a = Playlist()
a.createPlaylist()