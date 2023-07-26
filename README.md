# Inflation and average salary rate from 2007 to 2050

Rate shows comparison to 2007's data

## Installation

Clone the repository

```shell
$ git clone https://github.com/open-data-kazakhstan/inflation-and-avg-salary-with-projections.git
```
Requires Python 3.11.3 

Create a virtual environment and activate it 

```bash
pip install venv
python -m venv /path/to/localrepo
```
Swicth to venv directory by using cd comand
```bash
cd /path/to/localrepo
Scripts/activate
```

Install dependecies in venv by using pip
```bash
pip install -r requirements.txt
```
Run the project:
```bash
python scripts/main.py
```

## Data 

Sourse data handly collected from stat.gov stats: https://stat.gov.kz/

We downoladed data from that source and located it in acrhive as source.xsls

We have processed the source data to make it normalized and derived  several aggregated datasets from it:

* `archive/source.xsls` - sourse data 
* `acrhive/kazpop.csv` - unpivoted sourse data 
* `data/csv_final.csv` - expanded main dataset which predicts populations from 2023 to 2050
* `data/rsl1.csv` - final dataset expanded to 10 steps to make vizualization smoother
* `datapackge.json` - conatins all of the key information about our dataset
