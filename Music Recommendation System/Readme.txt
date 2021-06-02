songs: contains id for songs   (9938 x 1) 
user: contains user id              (3863 x 1)  
meta : contains meta data like song id, artist name, year ,title  
song_feature : 9938 x 5 feature vectors      # most important 
user_features: 3863 x 5 feature vectors      # most important

song features and user features are extracted using collaborative filtering.
songs features may have the data like, the extent of excitement, extent of  romance etc
while user features have the data like, how much the user like excitement in song, how much the user like romance in the song, etc


-> Upcoming Recommendation would be based of user profile and Song profile clusters.
-> Autogeneration of playlist according to user's mood
