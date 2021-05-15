Research : - Predicting outcome of football matches  using Convolution neural network

Trying to predict the outcome of football matches as win, loss or draw. I am trying to use the combination of player attributes, team attributes and match attributes. 

Europian Soccer dataset :- https://www.kaggle.com/hugomathien/soccer

model.ipynb = Predict using combination of player features, team features, and other match related features
PlayerDetailsPrediction.ipynb = Predict using only player attributes
TeamAttributesPrediction.ipynb = Predict using only team attributes
PreProcessing.ipynb = Reorganize the given dataset and combine player, team and match features into one dataset 

Player attributes 

Overall Rating
Potential
Crossing
Finishing
Heading accuracy
Dribbling
Free Kick accuracy
Ball Control
Sprint Speed
Acceleration
Strength
Long shots
Aggression
Positioning
Interceptions
Penalties
Making
Stamina
Shot power


Team Attributes

Build-up play speed
Build-up dribbling
Build-up passing
Chance creation passing
Chance creation crossing
Chance creation shooting
Defense pressure
Defense aggression
Defense teamwidth

Other attributes ( Match related features) 

League id
Season
Home team id
Away team id
Home team player 1 -11
Awat team player 1- 11
Country id 


Classes 

Home Win = +1
Home loss = -1
Draw = 0

Team attributes

All the team attributes are being compared between home team and away team. 
Each cell is filled with home feature value - away feature value 
Size 9x9 = 81 compared values

Player Attributes

All the player attributes each compared between home players and away players . Each cell represents  value for 
 Cell value = home player value for feature 1 - away player value for feature 1
For 19 features we have 19 layers each size of 11x11 = 121 . 
Each layer compares the difference about a one feature of away team and home team. (eg: overall rating )

Size = 11x11x1

Apply 1x1x19 and reduce the neural network to size 11x11x1 

Other attributes

Other feature size = 27


All features of size  = 121 + 81 + 27 = 229

In put into the neural network for prediction.

