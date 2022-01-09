Feature: FizzBuzz
	Sprawdzenie czy FizzBuzz zwraca to co powinien.

	Scenario: Input value equals 3:
		Given FizzBuzz
		Then chcecking if 3 gives Fizz

	Scenario: Input value equals 9:
		Given FizzBuzz
		Then chcecking if 9 gives Fizz

	Scenario: Input value equals 27:
		Given FizzBuzz
		Then chcecking if 27 gives Fizz

	Scenario: Input value equals 5:
		Given FizzBuzz
		Then chcecking if 5 gives Buzz

	Scenario: Input value equals 125:
		Given FizzBuzz
		Then chcecking if 125 gives Buzz

	Scenario: Input value equals 65:
		Given FizzBuzz
		Then chcecking if 65 gives Buzz

	Scenario: Input value equals 15:
		Given FizzBuzz
		Then chcecking if 15 gives FizzBuzz

	Scenario: Input value equals 90:
		Given FizzBuzz
		Then chcecking if 90 gives FizzBuzz

	Scenario: Input value equals 150:
		Given FizzBuzz
		Then chcecking if 150 gives FizzBuzz
