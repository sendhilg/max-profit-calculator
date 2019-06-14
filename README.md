# Max Profit Calculator

## Description
The application is completed as a task following the [brief](BRIEF.md).

## Requirements
The application was developed using python version 3.7.3.

To check the version on your machine run the below command:

    $ python --version

## Cloning the project and running the application
Clone the project from github. Change into the project directory 'max_profit_calculator'.

Enter the below command to accept input from the command line and press the enter key:

    $ python -m max_profit
    
Enter numeric price values seperated by space (e.g. 10 20 30) and press enter key to get the max profit.

To exit the prompt press ctrl+z(on windows) or ctrl+d(on linux) and press the enter key.

### Example
```
$ python -m max_profit

Enter stock prices (values seperated by space e.g. 10 20.5 30.25 5 7) to get the max profit:

10 20 30 40 50

Max profit: 40.0 (Buying for $10.0 and Selling for $50.0)

11.5 12.5 11 4 12

Max profit: 8.0 (Buying for $4.0 and Selling for $12.0)

```

## Unit Tests

### Prerequisites
pytest library is required for running the application's unit tests. Install pytest, also optionally install pytest-cov if the code coverage needs to be checked.

    $ pip install pytest
    $ pip install pytest-cov

### Running unit tests
Navigate to the repository and run the below command to execute the unit tests.

    $ pytest

Run the below command to execute tests displaying code coverage.

    $ pytest --cov=max_profit tests/
