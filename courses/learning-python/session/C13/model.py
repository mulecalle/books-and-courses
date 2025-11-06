# The model knows nothing about the view or the controller.

# Modules out house
import time
import os

# Modules in house
from src import jsondata

class Model:

    # Variable to shown
    current_function = ''
    remaining_time = ''
    pass_count = ''
    fail_count = ''
    skip_count = ''

    # Auxiliary variables to handle the execution time
    start_time = ''
    total_estimated_run_time = ''

    def __init__(self, regression_name):

        self.current_function = ''
        self.pass_count = 0
        self.fail_count = 0
        self.skip_count = 0

        # time should be handle in minutes
        self.start_time = time.time()
        self.total_estimated_run_time = self.get_original_estimated_run_time(regression_name)
        self.remaining_time = self.total_estimated_run_time


    def get_original_estimated_run_time(self,regression_name):
        # get run time estimation data from a json file

        try:

            current_dir = os.path.dirname(__file__)
            json_dir = os.path.join(current_dir, 'data\\regression_estimated_runtime.json')
            json = jsondata.read_json(json_dir)
            value = json.get(regression_name)

            if value is None:

                return 'not_define'

            return value

        except:

            return 'not_define'

    def calculate_remaining_time(self):
        # estimate the remaining run time according the values that we have

        if self.total_estimated_run_time is None:

            current_time = time.time()

            # Calculate the execution time
            elapsed_time = current_time - self.start_time

            # Calculate remaining time
            current_remaining_time = float(self.total_estimated_run_time) - (elapsed_time/60)

            self.remaining_time = int(current_remaining_time)


    def increase_pass_count(self):
        self.pass_count += 1
        self.calculate_remaining_time()

    def increase_fail_count(self):
        self.fail_count += 1
        self.calculate_remaining_time()

    def increase_skip_count(self):
        self.skip_count += 1
        self.calculate_remaining_time()

    def set_current_function(self, function_name):
        self.current_function = function_name
        self.calculate_remaining_time()

    def get_model(self):

        # create a dictionary with the data of the model
        dict = {'function': self.current_function,
        'TTend': self.remaining_time,
        'pass': self.pass_count,
        'fail': self.fail_count,
        'skip': self.skip_count}

        return dict