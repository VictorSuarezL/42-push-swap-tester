# 42 Push Swap Tester

This is a tester for the 42 Push Swap project. It is designed to test the functionality and correctness of the push_swap program.

## Usage

To run the tester, make sure you have Python 3 installed on your system. Then, follow the steps below:

1. Clone the Push Swap project repository.
2. Navigate to the directory where the push_swap program is located.
3. Copy the `run_push_swap.py` file from this tester repository into the same directory.
4. Open a terminal and navigate to the directory where the push_swap program and `run_push_swap.py` file are located.
5. Run the tester by executing the following command:

   ```bash
   python3 run_push_swap.py
    ```
6. The tester will display the results of the tests and output the number of tests passed and failed.
7. If any of the test is over the maximum for +5pts in the evaluation it will save a .txt file with the test that failed.

## Customizing the Tester

You can customize the behavior of the tester by modifying the following variables in the `run_push_swap.py` file:

- `batch`: The number of tests to run in each batch. The tester will run `batch` tests and display the results before moving on to the next batch. 
- `number_to_test`: The number of random numbers to test the push_swap program with. By default, the tester will test the program with 5, 100, and 500 random numbers.

## Contributing

If you encounter any issues with the tester or have suggestions for improvements, feel free to open an issue or submit a pull request.
