# ETF Analyzer
In this analyzer, I build a financial database and web application by using SQL, Python, and the Voilà library to analyze the performance of a hypothetical fintech ETF.

---
# Technology

This project uses Python 3.7 and the associated packages:

* [pandas](https://github.com/pandas-dev/pandas) - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more.

* [hvplot.pandas](https://pypi.org/project/hvplot/) - A high-level plotting API for the PyData ecosystem built on HoloViews.

* [jupyter notebook](https://jupyter.org/) -J upyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning.

* [sqlalchemy](https://www.sqlalchemy.org/) - the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

* [voila](https://pypi.org/project/voila/) - Rendering of live Jupyter notebooks with interactive widgets.

Installation Guide

Install the app's dependencies first.

```
  pip install pandas
  pip install sqlalchemy
  pip install hvplot
  pip install voila
```
---

# Useage

Download all the requirement data including etf.db and etf_analyzer.ipynb

Run the etf_analyzer.ipynb with jupyter notebook in jupyter lab.

Run voila in CLI with command
```
voila etf_analyzer.ipynb
```
![image](Voila.gif)

---

## Contributors
FinTech Team


---

## License

[MIT](https://choosealicense.com/licenses/mit/)