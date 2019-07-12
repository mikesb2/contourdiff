# Contourdiff
ContourDiff is a vector-based visualization over contour plots to analyze the trends of change across spatial regions and temporal domain. ContourDiff is written in python. ContourDiff first, aggregates for each location, the information around the neighbouring points over the temporal domain and then, creates a vector field that extracts the vectors associated to the contour paths. Finally, it overlays the
prominent vectors along the contour paths, revealing the differential trends that the contour lines experienced over time. 

This readme explains how to set-up and use this code as well as the Dataset Description and input data format.

# Dataset Description
Our approach is applicable to any spatiotemporal dataset, which is spatially continuous. The data can be represented as positive matrices, each corresponding to a single time sample.
In this paper, we have used Weather Research and Forecasting (WRF) model output as a case study. WRF has been one of most used and steadily growing atmospheric model for research and numerical weather prediction with over 36,000 registered users and over 1,340 peer reviewed publications. The observed dataset contains data values related to 26 parameters from January 2013 to September 2015 over western Canada (latitude X longitude). As a case study for this research, we examine the following parameters: soil moisture (SMOIS), land surface temperature (TSK), and downward long wave flux at ground surface (GLW) using to show trends. The dataset used for this work has the size 639 X 699 with a resolution of 4km. 

# Libraries used for implementation
Name	       Version 	      Description
Pandas	     0.23.4	    This module is used to create a dataframe from the input CSV files to do further analysis and computation.
Numpy	       1.15.4	    This module is used to create 2-dimensional arrays from the dataframe and perform the required computation before                         plotting the resultant values as a figure.
Matplotlib	 3.0.2	    This module is used to display figures from computation performed based on user input.
