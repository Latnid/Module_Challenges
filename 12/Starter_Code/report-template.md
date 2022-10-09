# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* The purpose of this analysis is to find out which model is better, the one trained with original data or the one trained with the resampled data.

* The data is historical lending activity from peer-to-peer services, in this analysis the model will pridict the risky loans over all the loans.

* The variable the model trying to predict is y, which repersense the column 'loan_status'.

* In this analysis, I have created two models, the first one using the original data(Module 1), then I use resampled (overresampling) to creat the resample data for training  Model 2. Base on the accuracy and classification report，I decide which one is better.

* I used LogisticReression as the majority model, RandomOverSampler as the resample model.

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
Model 1 has the accuracy 95%, the report shows precision and recall scores as follow:

                pre       rec       spe        f1       geo       iba       sup

        0       1.00      1.00      0.92      1.00      0.95      0.92     18741
        1       0.87      0.92      1.00      0.89      0.95      0.90       643

avg / total     0.99      0.99      0.92      0.99      0.95      0.92     19384


* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
Model 2 has the accuracy 99%, the report shows precision and recall scores as follow:

                   pre       rec       spe        f1       geo       iba       sup

          0       1.00      0.99      1.00      1.00      1.00      0.99     18741
          1       0.86      1.00      0.99      0.93      1.00      0.99       643

avg / total       1.00      0.99      1.00      0.99      1.00      0.99     19384


## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
All in all, the resampled data trained a better module. But they are not too much difference.

The results regarding accuracy of the minority class are actually mixed

First, the accuracy score is higher for the resampled data (0.99 vs 0.95), meaning that the model using resampled data was much better at detecting true positives and true negatives.

Then, the precision for the majority class maintain the same(1 vs 1), meaning that the original data was the same at detecting healthy loan('0'). For the minority class, the precision is 0.01 less than the orginal data, which means the origin model is better on detecting high-risk loan('1').

lastly, in terms of the recall,the majority class metric using original data was better (1 vs 0.99). Meaning that the original data correctly clasified a higher percentage of healthy loan.For the minority class, the model metric using resampled data was better(1 vs 0.92),which means the resampled model is better on detecting high-risk loan('1').

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

If you do not recommend any of the models, please justify your reasoning.

The Module 2 is better on predict '1' which is the high-risk loan. If the company are focus on find the high-risk loan. Module two is a better option. If the company is only want to identify the healthly loans, then the Module 1 already can do the job.


# Technology

This project uses Python 3.7 and the associated packages:

* [pandas](https://github.com/pandas-dev/pandas) - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more.

* [hvplot.pandas](https://pypi.org/project/hvplot/) - A high-level plotting API for the PyData ecosystem built on HoloViews.

* [jupyter notebook](https://jupyter.org/) -J upyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning.

* [sklearn](https://scikit-learn.org/) - Simple and efficient tools for predictive data analysis.Open source, commercially usable - BSD license

Installation Guide

Install the app's dependencies first.

```
  pip install pandas
  pip install -U scikit-learn
  pip install hvplot
```
---

# Useage


Download all the requirement data including Resources folder and credit_risk_resampling.ipynb

Run the credit_risk_resampling.ipynb with jupyter notebook in jupyter lab.



---

## Contributors
FinTech Team


---

## License

[MIT](https://choosealicense.com/licenses/mit/)