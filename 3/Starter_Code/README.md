# Crypto arbitrage analysis

Users may use this analysis to find out when is the best time to become arbitrageurs.
This analysis uses the data from 2018-01-01 to 2018-03-31 from two different exchanges.These two exchangers are Bitstamp and Coinbase. I take three different days from early, middle and late from these data and compare the conclusion. This analysis can help decide to target arbitrage opportunities in Bitcoin throughout the time frame.

---

## Technologies

This project uses Python 3.7 and the associated packages:

* [pandas](https://github.com/pandas-dev/pandas) - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more.

* [pathlib](https://github.com/budlight/pathlib) - pathlib offers a set of classes to handle filesystem paths. 

* [jupyter notebook](https://jupyter.org/)-JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionalit

Installation Guide

Install the app's dependencies first.

```python

  pip install pandas
  pip install pathlib

```

---

## Usage

Download all the requirement data including csv files
Store all csv files in Resources folder.

[bitstamp.csv](Resources/bitstamp.csv)
[coinbase.csv](Resources/coinbase.csv)

Run the crypto_arbitrage.ipynb with jupyter notebook in jupyter lab.
The crypto_arbitrage.ipynb should located at the same directory of the Resources folder

---

## Contributors
FinTech Team
VP
A high-tech investment firm

---

## License

MIT License