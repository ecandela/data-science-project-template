# data-science-project-template
Project directory structure and scripts

Template repository for new data science projects. It's designed to work along with CRISP-DM methodology. 


#### Getting Started

This template is required when you want to start a repository with a data-science structure template

After creating the repository, the following bat files must be executed:

**00.create_env.bat :**  This bat file creates a virtual environment for the specific project into the **env** directory

**01.Install.bat :**  This bat file installs all the packages listed in **requirements.txt** into the **env** directory that was created in the step 1. 

**02.Install_jupyter_spyder.bat :**  This bat file installs jupyter (IDE) and spyder kernels (just dependencies). 

**03.start_jupyter.bat :** This bat file launches Jupyter Notebook in the browser.

**04.Install_geopandas.bat :** This step is **optional**. If you need geopandas dependencies then you must run the Install_geopandas.bat file.


#### Directory structure

The final directory structure should look like this, with the new directory **env**.

+ config
    + img_readme
    + whl
+ env
+ src
+ .gitignore
+ 00.create_env.bat
+ 01.Install.bat
+ 02.Install_jupyter_spyder.bat
+ 03.start_jupyter.bat
+ 04.Install_geopandas.bat
+ README.md
+ requirements.txt

#### Complementary directories/files

Name | Description
------------- | -------------
img_readme  | readme images
whl  | wheel files for geopandas


#### src directory

It is important to use CRISP-DM as a methodology and process model to guide data mining projects. For that reason, there will be a directory for each of the six phases of CRISP-DM.

![Image text](https://github.com/ecandela/data-science-project-template/blob/main/config/img_readme/crisp_process.jpg)

+ **src**
    + _BD_
    + _common_
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



