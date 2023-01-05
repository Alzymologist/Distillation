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

After running all cells, you should see several tabs with widgets. Now you can try to enter data manually from the provided data sets or load the state from `20221223_Test_Example.json` (it is in the `json` folder).

### Example dataset № 1
This data set contains only the values that are important for calculations. This dataset should show be "all green" (show no statistical warnings), see image below.

<img width="410" alt="Distillation - ok" src="https://user-images.githubusercontent.com/69721131/209453721-586c9520-c5f1-4c47-a9e3-25c968cc0558.png">

| Parameter                               | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.0660 | 81.1460 |
| Mass of pycnometer (with distillate), g | 80.5227 | 80.6018 |
| Mass of pycnometer (with residue), g    | 81.3434 | 81.4235 |
| pH                                      | 4.330   | 4.314   |


### Example dataset № 2
This data set contains only the values that are important for calculations. This dataset should show some statistical warnings, see image below.   

<img width="410" alt="Distillation - warnings" src="https://user-images.githubusercontent.com/69721131/209453657-dcf3b58f-a5b8-4c53-925d-861fa8152020.png">

| Parameter                               | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.4130 | 81.4907 |
| Mass of pycnometer (with distillate), g | 80.3232 | 80.4118 |
| Mass of pycnometer (with residue), g    | 81.8783 | 81.9567 |
| pH                                      | 4.310   | 4.330   |

### State loading
State loading creates a union state. If you currently have state A and loading state B, you get the union of states A and B, with priority for B. Example:   
   
State A   
widget1: valueX   
widget2:   
widget3: valueY   

State B   
widget1:   
widget2: valueP   
widget3: valueZ   

Union of states A and B   
widget1: valueX   
widget2: valueP   
widget3: valueZ   

### Creating report PDF
Once you have entered the data manually or loaded the state, you can go to the "Create report" tab, choose what to include in the report, and generate the report.   

## To do
* Add functions for color and bitterness calculations.   
* Check existing functions and data inside `update()` for correctness.   
