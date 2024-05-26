from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert hello_solution.hello("Craftsman") == "Hello, World!"
        assert hello_solution.hello("Mr. X") == "Hello, World!"

    

