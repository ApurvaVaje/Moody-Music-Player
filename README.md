# Moody-Music-Player
A basic recommendation system (music player) which  plays songs according to person's mood using Content-based learning.

ABSTRACT:

This is basically a music player that tries to gauge your mood and then tries to predict the next song you would like to listen. 
Basically we take 3 factors into consideration -  genre(mood), artist, album.
Songs are selected on grounds of mood first and then if it does not work, artist and album are taken up one by one. 
As it runs on your folder you can run it on your playlist and it will be adjusted to your mood. This makes use of machine learning concept of target function for prediction of mood and selection of music.

SOFTWARE REQUIREMENTS :
Windows 10 (64 bit) ,
IDLE (Python 3.6 64 bit) ,
JetBrains Pycharm Community Edition 2018.3.5 ,
Pygame 

THEORY:

Target Representation:

Target function is used to predict the song the user would want to listen to next. For this reason, a target function is defined with weights varying as the program proceeds.
T = W1G + W2Ar  + W3Al

	Where, G = 1, if genre(mood) of given song is same as current song.
	    = 0, otherwise
	Ar = 1, if artist of given song is same as current song.
	    = 0, otherwise
	Al = 1, if album of given song is same as current song.
	    = 0, otherwise

Iterative Hill Climbing:

In Iterative Hill Climbing, we chose a point at random and try to go to closest local maxima or minima. We do this iteratively for a large number of times to get to global maxima or minima. 
In this moody player, we are choosing the first song randomly, if the user dislikes this song its relevant songs are played. If none of them are liked by user, another song with different mood altogether is selected and the same procedure is tried again.

ALGORITHMS

A) Start Algorithm

Precondition: Program started.
Postcondition: Music Player started with random song playing.
1) Directory Chooser is shown to user, so that the choice of folder containing music can be made.
2) All mp3 files in this folder are selected and their path is stored in a list.
3) Their metadata is stored in a pandas dataframe.
4) Weights of target function are initialized to (W1=1, W2=0, W3=0).
5) Position and dislike are initialized to zero. 
6) A window is shown on the console with label of current song and various buttons – Like, Dislike, Next Song, Previous Song, Stop Song
7) A random song is selected from the list and it starts playing.

B) Like Button Algorithm

Precondition: Like button was clicked on the music player window.
Postcondition: Weights of the target function are changed.
1) Weight of the variable where the position is at that instance, is incremented by 5.
2) Dislike is set to zero.

C) Dislike Button Algorithm

Precondition: Dislike button was clicked on the music player window.
Postcondition: Weights of the target function are changed.
1) Dislike is incremented by 1.
2) Position goes to the next variable.
3) The weight of position is incremented by 1.
4) Next song function is called.

D) Next Song Button Algorithm

Precondition: Next Song button was clicked on the music player window.
Postcondition: Next song starts playing
1) Best Song function is called to get the next to play.
2) The song returned as best song is played.

E) Best Song Algorithm

Precondition: Dataframe is filled and target weights are set.
1) If dislike is more than 2,
  a)Mood function is called.
  b)Song returned by this function is returned.
2)Else
  a)Target function is calculated for all songs.  
  b)The song with max value is returned.

F) Mood Algorithm

Precondition: Dataframe is filled.
1) Dislike and position are initialized to zero. 
2) Weights are initialized to (1,0,0).
3) A random song with a different genre than the current song is returned.

STAGES OF PROJECT

1) A Basic Music Player

  Tkinter was used to created the GUI for the music player with buttons - Like, Dislike, Next Song, Previous Song, Stop Song. Pygame module was used to play the songs using its mixer library. Directory Chooser is used to go to folder containing the songs. Mp3 files in this are read into a list of songs which store their paths.


2) Metadata filled into Dataframe

  A pandas’ Dataframe is created for songs with columns – title, artist, album, genre. When the mp3 files are read into the song list, their metadata is extracted using EasyID3 library of Mutagen module and filled into the dataframe line by line.

3) Target Function Implementation

  Target function is defined and weights are initialized. If the user likes the song, weight of the category on grounds of which the song was selected is incremented by 5. If the user dislikes the song, the category adjacent to the category, on grounds of which the song was selected is incremented by 1.
	As initially the song is selected at random, if there is no similarity between the users liking and current song, i.e. if dislike is pressed 3 times, a song with a different mood is selected at random. 



