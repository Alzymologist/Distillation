# Distillation
Jupyter notebook for easy beer analysis.

## Dependencies
* Python 3.10 environment with `jupyterlab`, `ipywidgets`, `uncertainties` and `json` packages.
* pdflatex.


You can use conda to install Python dependencies. Installation using `ENV.yml` from source folder:

```shell
conda env create -f ENV.yml
```
## Using notebook
0) Activate the Python environment.
1) Start Jupyter lab.
2) Open Distillation.ipynb notebook.
3) Run all cells.

You should see several tabs with widgets. Now try to input data from supplied dataset 1 or 2.

### Example dataset № 1
This data set contains only the values that are important for calculations. This dataset should trigger no warnings (see image below).

<img width="380" alt="Distillation - JupyterLab1" src="https://user-images.githubusercontent.com/69721131/208796320-5f2c0698-b376-4bfe-9ea6-318607305e1c.png">

| Parameter                               | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.0660 | 81.1460 |
| Mass of pycnometer (with distillate), g | 80.5227 | 80.6018 |
| Mass of pycnometer (with residue), g    | 81.3434 | 81.4235 |
| pH                                      | 4.330   | 4.314   |


### Example dataset № 2
This data set contains only the values that are important for calculations. This dataset should trigger statistical warnings (see image below).

<img width="380" alt="Distillation - JupyterLab2" src="https://user-images.githubusercontent.com/69721131/208796553-ad4ddf19-6add-4862-ac7d-2206ce564fd9.png">

| Parameter                               | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.4130 | 81.4907 |
| Mass of pycnometer (with distillate), g | 80.3232 | 80.4118 |
| Mass of pycnometer (with residue), g    | 81.8783 | 81.9567 |
| pH                                      | 4.310   | 4.330   |


### Creating report PDF
Once you entered this data, got to the "Create report" tab, choose what to include in the report and generate it by clicking the button.

## To do
* Add functions for color and bitterness calculations.
* Create a data loading system. It will help to load widgets state after Kernel shut down and also to do testing.
* Check existing functions and data inside `update()` for correctness.
