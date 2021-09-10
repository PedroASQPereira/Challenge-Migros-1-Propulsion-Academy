Migros-Store-Location-Challenge
==============================

Data Challengue #1
Data Science Propulsion Bootcamp


**Objective:** To find the most profitable location for a new Migros supermarket in Zürich

**Description:** This project was choosen by us to become familiar with geodata and its multiple interfaces with python. 
Additionally we used the following methods throughout the project: 
    \n- *Data Gathering:*  Google Places API, Selenium, proprietary data from UrbanDataLab.
    - *Data Preparation and Understanding:* Pandas and Matplotlib
    - *Data Visualization:* Pydeck for scatter and heatmap rendering on map

**Methodology:** The project is based on the assumption that existing supermarkets are profitable and that the location of the supermarket plays a significantly role in the profitability. Therefore, further considerations shuold as customer segments and preferences will not be considered. The key phases of the project's methodology are the following:
    - *Step 1:* Select from available data the parameters correlated to existing Migros' locations
    - *Step 2:* Based on the parameters defined above, identify most attractive locations and exclude outliers
    - *Step 3:* Cross-check for number and type of existing supermarkets in these locations
    - *Step 4:* Compile relational models to make an evaluation 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
