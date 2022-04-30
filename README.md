# data-science-project-template
Project directory structure and scripts

#### Getting Started

After cloning the repository, the following bat files must be executed:

**00.create_env.bat :**  This bat file creates a virtual environment for the specific project into the ..\env directory

**01.Install.bat :**  This bat file installs all the packages listed in requirements.txt into the env directory that was created in the step 1. 

**02.Install_jupyter_spyder.bat :**  This bat file installs jupyter and spyder kernels (Not IDE). 

**03.start_jupyter.bat :** This bat file launches Jupyter Notebook in the browser.

**04.Install_geopandas.bat :** This step is **optional**. If you need geopandas dependencies then you must run the Install_geopandas.bat file.


#### Directory structure

The final directory structure should look like this, with the new directory env.

+ config
    + img_readme
    + whl
+ env
+ src
.gitignore
00.create_env.bat
01.Install.bat
02.Install_jupyter_spyder.bat
03.start_jupyter.bat
04.Install_geopandas.bat
README.md
requirements.txt

#### Complementary directories/files

Name | Description
------------- | -------------
img_readme  | readme images
whl  | wheel files for geopandas
requirements.txt  | Dependency list
requirements_geopandas.txt  | geopandas dependency list


#### src directory
all scripts, notebooks and datasets should be placed here.
+ src
    + Prj_BD
    + Prj_Core
    + Prj_Project_1
    + Prj_Project_2


Name | Description
------------- | -------------
Prj_BD  | directory for datasets
Prj_Core  | directory for common scripts
Prj_Project_1 | advanced analytics project 1
Prj_Project_2 | advanced analytics project 2

#### src/Prj_Project_1 directory

It is important to use CRISP-DM as a methodology and process model to guide data mining projects. For that reason, there will be a directory for each of the six phases of CRISP-DM.

![Image text](https://github.com/ecandela/data-science-project-template/blob/main/config/img_readme/crisp_process.jpg)

+ **src**
    + Prj_BD
    + Prj_Core
    + **Prj_Project_1**
        + _01_Business_Understanding
        + _02_Data_Understanding
        + _03_Data_Preparation
        + _04_Modeling
        + _05_Evaluation
        + _06_Deployment


Name | Description
------------- | -------------
_01_Business_Understanding  | Files that explain what your organization expects to gain from this project.
_02_Data_Understanding  | Files for taking a closer look at the data available for this project.
_03_Data_Preparation | Files that prepare the data for modeling
_04_Modeling | Files that estimate the model
_05_Evaluation | Files that evaluate the results using the business success criteria established at the beginning of the project.
_06_Deployment | Files to deploy the project in the organization



