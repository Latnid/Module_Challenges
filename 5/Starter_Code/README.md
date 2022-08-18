### Financial_planning_tools

This tool has two functions. 
Function 1: A financial planner for emergencies. The members will be able to use this tool to visualize their current savings. The members can then determine if they have enough reserves for an emergency fund.

Function 2: A financial planner for retirement. This tool will forecast the performance of their retirement portfolio in two period of time which is 30 years and 10 years. To do this, the tool will make an Alpaca API call via the Alpaca SDK to get historical price data for use in Monte Carlo simulations.

---
This project uses Python 3.7 and the associated packages:

* [pandas](https://github.com/pandas-dev/pandas) - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more.

* [pathlib](https://github.com/budlight/pathlib) - pathlib offers a set of classes to handle filesystem paths. 

* [alpaca_trade_api](https://github.com/alpacahq/alpaca-trade-api-python) -Python client for Alpaca's trade API

* [dotenv](https://pypi.org/project/python-dotenv/) -Read key-value pairs from a .env file and set them as environment variables

* [jupyter notebook](https://jupyter.org/)-JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionalit

Installation Guide

Install the app's dependencies first.

```python

  pip install pandas
  pip install pathlib
  pip install alpaca-trade-api
  pip install dotenv

```

---

## Usage

Download all the requirement data including MCForecastTools.py
Store MCForecastTools.py file in the same folder with financial_planning_tool.

[MCForecastTools.py](./"MCForecastTools.py")

Run the financial_planning_tools.ipynb with jupyter notebook in jupyter lab.

---

## Contributors
FinTech Team
A high-tech investment firm

---

## License

MIT License