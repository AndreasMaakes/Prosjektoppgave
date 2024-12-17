# README - Soil moisture estimation using CYGNSS

This is a python program written for the course TBA4560 - Geomatics, Specialization Course at NTNU Trondheim, which is a 15 study point course intended for 5th year students at the Department of Civil and Environmental Engineering. The project spanned the entire semester during autumn 2024, and was finished in December 2024. The purpose of the program is to fetch CYGNSS - Level 1 data using Pydap, filter the data, estimate the soil moisture, and then plot the results, all in the same program. Performing these steps manually would normally take a long time and require a considerable amount of disk space available on the local computer, but this program effectivizes the process, and makes it more sustainable.

In order to use the program, we assume you already have installed a Integrated development environment (IDE) like for example Visual Studio Code (VSCode). You also would need git to clone the project and pip, which is used to install the necessary dependencies. 

## Installing necessary dependencies

Because we have used various python libraries, installing these is necessary in order to run the program. This involves setting up a virtual environment, entering the environment, and installing the dependencies. 


### Setting up the virtual enviroment

Head to the root folder of the project (replace the path below with your local path):

```bash
cd ~/Desktop/my_project
```

Create the virtual enviroment:

```bash
python -m venv venv
```

### Activate the environment:

For macOS:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### Installing the dependencies

When inside the venv, you install the dependencies for the project by using the following command:

```bash
pip3 install -r requirements.txt
```

## Running the program

The program is structured in such a way that each central part of the process can be run independently. This means the plotting of the results can be performed without having to perform the data-fetching and filtering if this has already been done prior. The steps for performing the data handling and the plotting are given below:

### Data handling

The part of the program that fetches the data, filters the data, and calculates the surface reflectivity (SR) is located in the folder "dataHandling". Inside this folder there are python files containg the logic corresponding to the different parts of the data handling, but in order to run the program we only need the file main.py. Inside this file you can adjust parameters such as the geospatial filter, the temporal filter, and other parameters used for the data filtering. Then you just need to run the main.py file and the data handling will initiate. A progress bar will appear in the terminal, showing how much of the CYGNSS data is fetched and filtered at any time.

### Plotting

When data is fetched and filtered it is stored inside the "data" folder, and is now ready to be plotted. We have implemented two types of plots, and the code for these are located inside the "plotting" folder. Along with these is the main plotting file called "plotting.py". 
