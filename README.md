# Distillation
Jupyter notebook for easy beer analysis.

<img width="800" alt="Distillation-index" src="https://user-images.githubusercontent.com/69721131/205592542-f70a4f35-ddee-4cf1-8eb8-dcdddbc64678.png">

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

You should see several tabs with widgets. 

### Example dataset № 1
This dataset should trigger no warnings.

| Parameter                               | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.0660 | 81.1460 |
| Mass of pycnometer (with distillate), g | 80.5227 | 80.6018 |
| Mass of pycnometer (with residue), g    | 81.3434 | 81.4235 |
| pH                                      | 4.330   | 4.314   |


### Example dataset № 2
This dataset should trigger several warnings.

| Parameter                               | Series1 | Series2 |
|-----------------------------------------|---------|---------|
| Mass of pycnometer (empty), g           | 30.6907 | 30.7931 |
| Mass of pycnometer (with water), g      | 80.7730 | 80.8525 |
| Mass of pycnometer (with beer), g       | 81.4130 | 81.4907 |
| Mass of pycnometer (with distillate), g | 80.3232 | 80.4118 |
| Mass of pycnometer (with residue), g    | 81.8783 | 81.9567 |
| pH                                      | 4.31    | 4.33    |

Once you entered this data, select what to include in the report and generate the report by clicking the big button.

## To do
1) Add functions for color and bitterness calculations.
2) Create a data loading system. It will help to load widgets state after Kernel shut down and also to do testing.
3) Check existing functions and data inside `update()` for correctness.
