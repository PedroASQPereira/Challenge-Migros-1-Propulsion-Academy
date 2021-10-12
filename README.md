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
