Migros-Store-Location-Challenge
==============================

Data Challengue #1

Data Science Propulsion Bootcamp


**Objective:** To find the most profitable location for a new Migros supermarket in Zürich

**Description:** This project was choosen by us to become familiar with geodata and its multiple interfaces with python. 
Additionally we used the following methods throughout the project: 
    
- *Data Gathering:*  Google Places API, Selenium, proprietary data from UrbanDataLab.
- *Data Preparation and Understanding:* Pandas and Matplotlib   
- *Data Visualization:* Pydeck for scatter and heatmap rendering on map

**Methodology:** The project is based on the assumption that existing supermarkets are profitable and that the location of the supermarket plays a significantly role in the profitability. Therefore, further considerations shuold as customer segments and preferences will not be considered. The key phases of the project's methodology are the following:

- *Step 1:* Select from available data the parameters correlated to existing Migros' locations
- *Step 2:* Based on the parameters defined above, identify most attractive locations and exclude outliers
- *Step 3:* Cross-check for number and type of existing supermarkets in these locations
- *Step 4:* Compile relational models to make an evaluation 

**Visualization:**
The figure below illustrates the number of supermarkets and Migros suoermarkets in Zürich obtained from the Google API platform. In green are displayed all supermarkets and in orange the Migros.

![image](https://user-images.githubusercontent.com/37544176/132989865-bdd44bea-c288-4b52-b2c6-790691e3c877.png)


Additionally, one of our models returned the following heatmap:

![image](https://user-images.githubusercontent.com/37544176/132990032-26a32443-5e33-41fa-8b6d-05cea1c985d5.png)

As it can be observed, there are multiple isolated points with varying degrees of gradients. To derive conclusion from the map, it is required not only to analyse the corresponding gradient and the size of the cluster. For example, isolated squares should not be considered, regardless of their respective benefit, because it might be that supermarkets are already present on the neighbouring squares.

**Conclusions:**

In this project, we familiarized ourselves with data gathering tools (APIs and Web scraping), data manipulation and preparation, data visualization tools and a set of linear models. 

**Future work:**

- Varying the size of the squares: Start with large areas identifying the locations with the lowest number of supermarkets and the split it into smaller pieces to identify specific locations
- Introducing more features into the model: Currently only number of supermarkets, population density and transportation quality are considered. Other factors influencing the profitability of a supermarket would be average income, rent, traffic levels, etc.

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
