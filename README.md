# Distillation
Jupyter notebook for easy beer analysis

### Dependencies
* Python 3.10 environment with `jupyterlab`, `ipywidgets`, `uncertainties` and `json` packages
* pdflatex

You can use conda to install Python dependencies. Installation using `ENV.yml` from source folder:

```shell
conda env create -f ENV.yml
```
### Using notebook
0) Activate the Python environment
1) Start Jupyter lab
2) Open Distillation.ipynb notebook
3) Run all cells

You should see several tabs with widgets. Example of data to play with:

| Value                                   | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.4130 | 81.4907 |
| Mass of pycnometer (with distillate), g | 80.3232 | 80.4018 |
| Mass of pycnometer (with residue), g    | 81.8783 | 81.9567 |
| pH                                      | 4.31    | 4.33    |

Once you entered this data, select what to include in the report and generate the report by clicking the big button.

### To do
0) Write functions for calculating averages and uncertainties (marked by "average_" in names). At the moment only the function for ABV is ready, other functions are placeholders, that return only averages. See functions in `defined_lab_functions.py`
1) Add functions for color and bitterness calculations.
2) Create a data loading system. It will help to load widgets state after Kernel shut down and also to do testing.
3) Check existing functions and data inside `update()` for correctness.