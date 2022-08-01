<h1 align='center' style='color:purple'>Sonar - Mines vs Rocks</h1>

### Project Discription:
The focus of this project will be the Sonar Mines vs Rocks dataset. The problem is to predict metal or rock objects from sonar return data. The file "Sonar_Mines_vs_Rocks.csv" contains 208 patterns (97 patterns for rocks, 111 patterns for Mines) obtained by bouncing sonar signals off a metal cylinder at various angles and under various conditions. The transmitted sonar signal is a frequency-modulated chirp, rising in frequency. The data set contains signals obtained from a variety of different aspect angles, spanning 90 degrees for the cylinder and 180 degrees for the rock.

Each pattern is a set of 60 numbers in the range 0.0 to 1.0. Each number represents the energy within a particular frequency band, integrated over a certain period of time. The integration aperture for higher frequencies occur later in time, since these frequencies are transmitted later during the chirp.

The label associated with each record contains the letter "R" if the object is a rock and "M" if it is a mine (metal cylinder). The numbers in the labels are in increasing order of aspect angle, but they do not encode the angle directly.


### Deployment: 
The application of this project is deployed to Heroku, it can be found in https://md-sonar-mines-vs-rocks.herokuapp.com

To test the application we can use, as an example, the first and last paterns which respectievly represents Rock and Mine:

Rock:

0.0453, 0.0523, 0.0843, 0.0689, 0.1183, 0.2583, 0.2156, 0.3481, 0.3337, 0.2872, 0.4918, 0.6552, 0.6919, 0.7797, 0.7464, 0.9444, 1.0, 0.8874, 0.8024, 0.7818, 0.5212, 0.4052, 0.3957, 0.3914, 0.325, 0.32, 0.3271, 0.2767, 0.4423, 0.2028, 0.3788, 0.2947, 0.1984, 0.2341, 0.1306, 0.4182, 0.3835, 0.1057, 0.184, 0.197, 0.1674, 0.0583, 0.1401, 0.1628, 0.0621, 0.0203, 0.053, 0.0742, 0.0409, 0.0061, 0.0125, 0.0084, 0.0089, 0.0048, 0.0094, 0.0191, 0.014, 0.0049, 0.0052, 0.0044

Mines: 

0.026, 0.0363, 0.0136, 0.0272, 0.0214, 0.0338, 0.0655, 0.14, 0.1843, 0.2354, 0.272, 0.2442, 0.1665, 0.0336, 0.1302, 0.1708, 0.2177, 0.3175, 0.3714, 0.4552, 0.57, 0.7397, 0.8062, 0.8837, 0.9432, 1.0, 0.9375, 0.7603, 0.7123, 0.8358, 0.7622, 0.4567, 0.1715, 0.1549, 0.1641, 0.1869, 0.2655, 0.1713, 0.0959, 0.0768, 0.0847, 0.2076, 0.2505, 0.1862, 0.1439, 0.147, 0.0991, 0.0041, 0.0154, 0.0116, 0.0181, 0.0146, 0.0129, 0.0047, 0.0039, 0.0061, 0.004, 0.0036, 0.0061, 0.0115

 

![Screenshot-13](https://user-images.githubusercontent.com/86875309/182231730-6ab0a594-7214-4d86-a261-123e184c16b8.png)
