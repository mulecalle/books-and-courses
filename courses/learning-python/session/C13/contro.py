# The controller understands both the model and the view.

# Modules in house
from view import View
from model import Model
import time

class Controller():

    def __init__(self, regressionName):

        self.model = Model(regressionName)
        self.view = View()
        self.model_update()


    def model_update_pass(self):
        self.model.increase_pass_count()
        self.model_update()


    def model_update_fail(self):
        self.model.increase_fail_count()
        self.model_update()


    def model_update_skip(self):
        self.model.increase_skip_count()
        self.model_update()


    def model_set_function(self, name):
        self.model.set_current_function(name)
        self.model_update()


    def model_update(self):
        state = self.model.get_model()
        self.view.update_content(state)


if __name__ == '__main__':

    mvc = Controller('name1')

    mvc.model_set_function('asd')

    mvc.model_update_pass()

    mvc.view.condition.notifyAll()

    mvc.model_update_pass()

    mvc.model_update_pass()

    mvc.model_update_pass()
