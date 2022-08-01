<h1 align='center' style='color:purple'>Sonar - Mines vs Rocks</h1>

### Project Discription:
The focus of this project will be the Sonar Mines vs Rocks dataset. The problem is to predict metal or rock objects from sonar return data. The file "Sonar_Mines_vs_Rocks.csv" contains 208 patterns (97 patterns for rocks, 111 patterns for Mines) obtained by bouncing sonar signals off a metal cylinder at various angles and under various conditions. The transmitted sonar signal is a frequency-modulated chirp, rising in frequency. The data set contains signals obtained from a variety of different aspect angles, spanning 90 degrees for the cylinder and 180 degrees for the rock.

Each pattern is a set of 60 numbers in the range 0.0 to 1.0. Each number represents the energy within a particular frequency band, integrated over a certain period of time. The integration aperture for higher frequencies occur later in time, since these frequencies are transmitted later during the chirp.

The label associated with each record contains the letter "R" if the object is a rock and "M" if it is a mine (metal cylinder). The numbers in the labels are in increasing order of aspect angle, but they do not encode the angle directly.


### Deployment: 
The application of this project is deployed to Heroku, it can be found in https://md-sonar-mines-vs-rocks.herokuapp.com



![Screenshot-13](https://user-images.githubusercontent.com/86875309/182231730-6ab0a594-7214-4d86-a261-123e184c16b8.png)
