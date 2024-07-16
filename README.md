# IPL Win Predictor App

## Overview

The IPL Win Predictor app forecasts the probability of winning or losing an IPL cricket match based on various match conditions and team performance metrics.

## Methodology
### Data Collection
- The dataset includes information such as:
  - Batting and bowling teams
  - Host city of the match
  - Target score set by the batting team etc

### Data Preprocessing
- **Feature Engineering:** Extract relevant features such as runs left, balls left, current run rate (CRR), and required run rate (RRR).
- **Normalization:** Scaling numerical features to ensure consistency in model training.
- **One-Hot Encoding:** Transform categorical variables like team names and city into numerical format.

### Model Building and Evaluation
1. **Logistic Regression**
   - Model trained using `LogisticRegression` from scikit-learn.
   - Evaluation metrics: Probability prediction for each team's win/loss.


### Model Evaluation
The models were evaluated based on:
- **Training Accuracy:** 80.3%
- **Test Accuracy:** 80%

### Model Selection
- **Logistic Regression** emerged as the preferred model due to its straightforward interpretation and competitive accuracy.
- **Random Forest** gives the best accuracy but not used due to its high values 
