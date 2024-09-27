# Molecule-solubility-prediction-app

This app is designed to predict the solubility of molecules. Its primary beneficiaries are biologists and chemists, enabling them to understand whether a molecule is soluble in water or other solvents using logS values.

A "logS" value represents the base-10 logarithm of a molecule's solubility, measured in moles per liter. Essentially, it indicates how well a molecule dissolves in water; a higher logS value signifies greater solubility, while a lower logS value indicates poorer solubility.

In this app, users can enter the descriptors of a molecule, and it will predict the logS value for that molecule.

##Data source : https://github.com/dataprofessor/data/blob/master/delaney_solubility_with_descriptors.csv

Here, I used two different machine learning approaches to achieve the best predictions:

1 Logistic Regression

2 RandomforestRegressor

After rewewing the metrics obtained from these two approaches,I decided to go with the RandomForestRegressor model.
![chart](https://github.com/user-attachments/assets/40948016-87cb-4acf-b451-ecfe60472f41)

### ScatterPlots:

![image](https://github.com/user-attachments/assets/675c0792-3f04-4b2a-b347-38190968d1b8)

![image](https://github.com/user-attachments/assets/f7042f1b-20ae-4758-9261-c052932551b4)

After finalizing the model, I stored both the model and the scaler as pickle files for use in the Flask application. The predictions are then displayed on an HTML page.

### Key processes in this project:

* ETL data using python libraries (pandas,numpy)
* Visualization using python library (matplotlib)
* Mechinelearning model creation(Linear Regression,RandomForestRegressor)
* Pickle
* Flask
* HTML
* CSS
* JavaScript
