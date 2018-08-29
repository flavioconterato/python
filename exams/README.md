# To execute a program:
## Python: 3.5.2
## PIP List:
*  Keras       2.2.2
*  Numpy       1.15.1
*  Pandas      0.23.4
*  Tensorflow  1.10.0

Example:
"pip install -U keras==2.2.2"

## Train:
##  python deepersystem.py -t file -r file
    python deepersystem.py -t train.csv -r traintruth.csv
####  "-t = train file"
####  "-r = train truth file"
####  Outputs:
####    Model(.json) and Weights(.h5) of slope and intercept:
####      model_slope.json , model_slope.h5, model_intercept.json , model_intercept.h5
      
## Test:
##  python deepersystem.py -n file
    python deepersystem.py -n test.csv
####  "-n = train file"
####  Outputs:
####    Predict text files of slope and intercept
####    slope_predict_test.txt
####    intercept_predict_test.txt
