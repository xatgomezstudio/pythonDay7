
from Chef import Chef
# gained access to that file

class ChineseChef(Chef):
#                ^ pass in the class we want to inherit from

    def make_special(self):
        print("The chef makes orange chicken")
    # if our inherited class has a class we want to over ride we can simply re-define the function here

    def make_friedRice(self):
        print("The chef makes fried rice")