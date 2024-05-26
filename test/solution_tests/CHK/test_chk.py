from solutions.CHK import checkout_solution


class TestSum():
    def test_sum(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("AAAABBBCCDD") == 325
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("123") == -1
        assert checkout_solution.checkout("F") == -1











