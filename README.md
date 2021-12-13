# Data Sciece Final Project

## Introduction
The purpose of the project was to create a model to help twitch streamers determine success. The model predicts follower growth given performance based metrics which streamers can use to determine how well they did by comparing to actual follower count in any given year.

![Website](https://raw.githubusercontent.com/salterdatwit/DataScienceFinal/main/Website.png)

## Selection of Data
The model training and testing were done in visual studeo code.

The dataset used consists of statistics about the top 1001 twitch streamers based on total watch time. Other statistics include stream time, peak viewers, average viewers, followers, followers gained, viewers gained, whether or not they were twitch partnered, if the stream was mature or not, and the language spoken.

![Data](https://raw.githubusercontent.com/salterdatwit/DataScienceFinal/main/Data.png)

Partnered and mature were converted into binary from yes/no in order to make it easier to work with.

We also used a pipeline to include features that were necessary for our model to return coherent data. 

![pipeline](https://user-images.githubusercontent.com/55757904/145746989-726f7a13-6d31-4739-a9a2-a5881ee4c280.png)

We changed the names of some streamers who had foreign character names into their translated names. We also used standard scalar to normalize. This resulted in roughly a 20% closer result in most cases.

## Methods
Tools:
* numpy
* pandas
* scikit-learn
* scipy
* flask

## Results
Our model had an R<sup>2</sup> value of around .568. This means that our model accounts for about 56.8% of the variance. While real data varies quite far, it provides a good baseline for follower growth and shows a trend. A higher number is also harder to achieve due to other variables that go into follower growth such as the streamers behaviour and advertising.

The model should not be used to determine growth for smaller streamers. The data was trained on the top 1001, so the follower growth will be much higher than it should be.

![Results](https://raw.githubusercontent.com/salterdatwit/DataScienceFinal/main/Results.png)

## Discussion
We experiented with SGD regression before ultimately settling on using lasso instead. We decided on a regression because we were predicting a quantity not a quality. We started with sgd because Devin forgot which way the aligator goes for greater than. We then decided to go with lasso.

## Summary
The project uses a supervised regression model to predict follower growth of big twitch streamers. The model breaks down when trying to predict follower growth for smaller streamers, but it still gets an R<sup>2</sup> value of around .568. Many variables account for channel growth so .568 is not a bad number for something like this. 

The model is live at http://73.60.142.217:5000/. 

