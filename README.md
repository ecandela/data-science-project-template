# data-science-project-template
Project directory structure and scripts
![Image text](https://github.com/ecandela/data-science-project-template/blob/main/config/img_readme/install.PNG)

#### Getting Started

After cloning the repository, the following bat files must be executed:

**1. create_env.bat :**  This bat file creates a virtual environment for the specific project into the ..\env directory

**2. Install.bat :**  This bat file installs all the packages listed in requirements.txt into the env directory that was created in the step 1. 

**3. start_jupyter.bat :** This bat file launches Jupyter Notebook in the browser.

**4. Install_geopandas.bat :** This step is **optional**. If you need geopandas dependencies then you must run the Install_geopandas.bat file.

**5. start_spyder.bat :** This step is **optional**. If you need geopandas dependencies then you must run the Install_geopandas.bat file.

#### Directory structure

The final directory structure should look like this, with the new directory env.

+ config
    + img_readme
    + whl
    + create_env.bat
    + Install.bat
    + Install_geopandas.bat
    + requirements.txt
    + requirements_geopandas.txt
    + start_jupyter.bat
    + start_spyder.bat
+ env
+ src

#### Complementary directories/files

Name | Description
------------- | -------------
img_readme  | readme images
whl  | wheel files for geopandas
requirements.txt  | Dependency list
requirements_geopandas.txt  | geopandas dependency list
