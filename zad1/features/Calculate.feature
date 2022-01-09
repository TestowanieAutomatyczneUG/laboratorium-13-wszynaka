Feature: Calculate
	Sprawdzenie czy Calculate zwraca to co powinno.

	Scenario: 3/1:
		Given Calculate
		Then chcecking if 3/1 gives 3

    Scenario: 66/2:
		Given Calculate
		Then chcecking if 66/2 gives 33

    Scenario: 80/40:
		Given Calculate
		Then chcecking if 80/40 gives 2

    Scenario: 333/111:
		Given Calculate
		Then chcecking if 333/111 gives 3

    Scenario: Error bcs of float:
		Given Calculate
		Then chcecking if float gives error