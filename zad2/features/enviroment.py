

from fizzbuzz.FizzBuzz import FizzBuzz


def before_scenario(context, scenario):
	context.fizz = FizzBuzz()

def after_scenario(context, scenario):
	context.fizz = None