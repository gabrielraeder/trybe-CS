from ex01 import fizzbuzz


def test_fizzbuzz_should_return_list_of_numbers():
    "Passando número 2 retorna [1, 2]"
    assert fizzbuzz(2) == [1, 2]


def test_fizzbuzz_divisible_by_three_should_be_fizz():
    "Passando número 3 retorna [1, 2, Fizz]"
    assert fizzbuzz(3)[-1] == "Fizz"


def test_fizzbuzz_divisible_by_five_should_be_buzz():
    "passando divisivel por 5 retorna Buzz"
    assert fizzbuzz(5)[-1] == "Buzz"


def test_fizzbuzz_divisible_by_five_and_three_should_be_fizzbuzz():
    "passando divisivel por 5 e 3 retorna FizzBuzz"
    assert fizzbuzz(15)[-1] == "FizzBuzz"
