<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/rmlz/cqw2calibtool">
  </a>

  <h3 align="center">CE-QUAL-W2 Calibration Tool</h3>

  <p align="center">
    A Python3 calibration tool for the CE-QUAL-W2 2-D Hydrodynamic and Water quality Model!
    <br />
    <br />
    <a href="https://github.com/rmlz/cqw2calibtool/issues">Report Bug</a>
    ·
    <a href="https://github.com/rmlz/cqw2calibtool/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![CE-QUAL-W2 Calibration Tool]](https://github.com/rmlz/cqw2calibtool)

To calibrate/optimize parameter values for a complex model such as CE-QUAL-W2 may be a time consuming task. This project aims on the automation of this task, so one can save time while searching the best suited parameter values for the modelling needs.

CE-QUAl-W2 Calibration tool was created to be easily modifiable, so it can be adapted to be used in any CE-QUAL-W2 model. Basically, it "re-creates" CE-QUAL-W2 control file before the automated execution of the model. 

This tool has been developed as a result of a MSc Degree work - Post-Graduate Program in Environmental Technology and Water Resources, Universidade de Brasília (UnB) - and it has been used to calibrate the temperature (hydrodynamics) and water quality of Brazil's mid-western reservoirs. 

First of all, before you start using this tool, its extremely recommended to read CE-QUAL-W2 Manual and be familiarized with its files, equations and etc. Then, it's very important to be aware of the dynamics you want to model. It has been found that the calibration tool may find inconsistent best values for some CE-QUAL-W2 parameters (data not published). In such manner, decisions must be taken before talking to an expert.


A list of commonly used resources that I find helpful are listed in the acknowledgements.
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo`, `twitter_handle`, `email`


### Built With

* [SPOTPY](https://github.com/thouska/spotpy)
* [Matplotlib](https://matplotlib.org/)
* [Numpy](https://numpy.org/)

<!-- GETTING STARTED -->

### Prerequisites

It's recommended model calibration proficiency, basic python programming skills and the use of the [Anaconda python distribution](https://www.anaconda.com/distribution/).

### Installation
 
1. Clone the repo
```sh
git clone https:://github.com/your_username_/Project-Name.git
```
2. Install requirements.
```sh
pip install .
```

<!-- USAGE EXAMPLES -->
## Usage

To use the calibration tool, you need to adapt different files to your own model. A  step-by-step guide for you to follow was created.

**Step 1 - Create a CE-QUAL-W2 model**
Before using this tool, it's strongly advisable to build the model, test it and do some manual calibration. The most familiarized you are to the CE-QUAL-W2 files, the most easy the adoption of this tool in your work will be . It's also recommended that you mantain the same folder structure of the example and/or move your project over the example folder.

**Step 2 - Editing .py files**
This step may take some time as you will need to adapt the Python files to your model. 

CE-QUAL-W2 control file may be huge (+/- 1000 lines) and even though to edit a .txt file may be an easy task, many errors can occur because of the simple mistyping of a space character.

**Here, you must pay strong attention to the editions you are doing.**

1. Go to cqw2_calibrate directory and open CQW2_spotpy_setup
This file contains the _spot_setup()_ class and some important functions:
```python
def parameters(self):
'''Generates the values of each calibrated parameter'''
def evaluation(self):
'''Takes observed data from a .csv file and use it to calculate objective function'''
def simulation(self, x):
'''Input the parameters values (x) to the CE-QUAL-W2 control file, executes the model and save its results'''
def objectivefunction(self, simulation,evaluation,params=None):
'''Calculates the objective function based on simulated and measured data'''
```

There's a string variable named **w2_connpt** in the _simulation(self, x)_ function. This string contains an entire CE-QUAL-W2 control (_w2_con.npt_) file. Many of its input values are coded into a dictionary variable named *paramname_paramvalue*.

2. Now, you must edit the **w2_connpt** variable for it to become your model's _w2_con.npt_. It's recommended to make copies from your project's control file, and then paste it into the variable.

Make sure that the **w2_connpt** variable contains every aspects of your model such as the number of branches. The available example model is a lake with four branches, and this aspect is included into the control file variable:
```python
'''
BRANCH G      US
BR1      '''+self.paramname_paramvalue['US_BR_1']+ '''
BR2      '''+self.paramname_paramvalue['US_BR_2']+ '''
BR3      '''+self.paramname_paramvalue['US_BR_3']+ '''
BR4      '''+self.paramname_paramvalue['US_BR_4']
'''
```
There are many variables that are branch discrepated and water bodies discrepated. **To be aware of which variables are branch/water body discrepated, refer to the CE-QUAL-W2 Manual.**

If a lower number of branches are needed, you must delete the unecessary entries inside the **w2_connpt**:

```python
''' Example with only 2 branches:
BRANCH G      US
BR1      '''+self.paramname_paramvalue['US_BR_1']+ '''
BR2      '''+self.paramname_paramvalue['US_BR_2']
'''
```

Instead, if you need to add a 5th branch into the control file (or new water bodies), you must create its respective dictionary entry. The entries can be added by editing the different .py files inside the **cqw2_calibrate** folder.  


E.G: In **branches.py** we have:
```python
branches = {
        #Branch Geometry
'upstream_segment' : [ #The number of entries must be the number in numb_water_branches
paramcontrol('US_BR_1', False,"      2",1,1,1),
paramcontrol('US_BR_2', False,"     22",1,1,1),
paramcontrol('US_BR_3', False,"     31",1,1,1),
paramcontrol('US_BR_4', False,"     37",1,1,1),

]
}
```

Here, the _paramcontrol()_ function, controls some useful aspects for calibration:

```python
def paramcontrol(name, calibrate, value, low, high, guess):
  '''
  name = Parameter or setting name,
  calibrate = boolean, True if the parameter must be calibrated (value will be not used)
  value = if calibrate = False, value will be inputed to the parameter field
  low = minimum value for calibration purposes
  high = maximum value for calibration purposes
  guess = optimum guess for calibration purposes
  '''
```

Going ahead, if a 5th branch is needed, you must add its entry to every branch discrete variable. For example purposes, a 5th branch entry is added into the _branches.py_ file inside **cqw2_calibrate** folder:

```python
branches = {
        #Branch Geometry
'upstream_segment' : [ #The number of entries must be the number in numb_water_branches
paramcontrol('US_BR_1', False,"      2",1,1,1),
paramcontrol('US_BR_2', False,"     22",1,1,1),
paramcontrol('US_BR_3', False,"     31",1,1,1),
paramcontrol('US_BR_4', False,"     37",1,1,1),
paramcontrol('US_BR_5', False,"     42",1,1,1),

]
}
```
**AGAIN! To be aware of which variables are branch/water body discrepated, refer to the CE-QUAL-W2 Manual.**

It's also necessary to change the file inputs such as QIN FILE TIN FILE and etc. You may find them at the end of the _w2connpt_ variable.

3. Now it is time to change the configuration of the calibrator. Open the CONFIG.py file inside **cqw2_calibrate** folder:

```python
config = {
        'W2_FILE': 'w2_con.npt', #w2con control file or path
        'WSC_FILE': 'wsc.npt', #wsc.npt file or path
        'EVALUATION_FILE': 'measured_data.csv', #MUST BE A CSV FILE WITH COLUMNS [Date, Data] IN THIS WORK >> [DATE, 0m, 1m, 5m, 10m, 1m to bottom]
        'SIMULATION_PATH': os.getcwd() + '\\Results\\CE-QUAL-W2\\', #Simulation output path
        'SIMULATION_FILE': ['time_series_1_seg18.opt','time_series_2_seg18.opt','time_series_3_seg18.opt','time_series_4_seg18.opt','time_series_5_seg18.opt'], #The names of the output files
        'OBJECTIVE_VARIABLE': ['T2(C)'] #The calibration objective variable column inside the configuration file;      
        }
```

You may change it and input the name of the files you want to use. 

4. There are several possible changes inside the **CQW2_spotpy_setup**. SPOTPY documentation are very clear about it, and has many examples of the objective functions and optimization algorithms use. Please, refer to its github before attempting to make any change: [SPOTPY](https://github.com/thouska/spotpy)

5. After all needed changes are done, now it's time to test the deployment of the **w2_con.npt** file. Just execute **run_model.py**. If you find any error by attempting to deploy the file and run the model:

First, again, it's strongly recommended to be familiarized with CE-QUAL-W2 errors and its preprocessor. Run the _preprocessor.exe_ and try to debug the control file by opening the deployed _w2_con.npt_ and checking for linebreaking or mistypings. Thus, resolve any problems found by editing the **w2connpt** variable or any of the entry .py files.

**CE-QUAL-W2 control file follows a right justified 8 characters long columns format, so ALWAYS be aware if the columns are correctly formated**

Here, keep looping into editing the **w2connpt** variable and executing _run_model.py_ until no more errors is found by the preprocessor and the model start looping into running and saving data to the Database.

This is a very simple tutorial. If you find any problems, you may ask me in the [open issues](https://github.com/rmlz/cqw2calibtool/issues) area of this github.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Ramon Pinto de Barros
[Email](mailto:pbarrosramon@gmail.com)
[Lattes Curriculum](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4419240A0)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

This work was done thanks to:
* [CNPq](www.cnpq.br) Post-Graduate Scolarship;
* [PTARH-UNB](www.ptarh.com.br) Post-Graduate Program in Environmental Technology and Water Resources, Universidade de Brasília (PTARH-UNB) supervision;



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
