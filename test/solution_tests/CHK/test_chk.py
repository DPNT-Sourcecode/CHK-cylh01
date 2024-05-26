from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert hello_solution.hello("Craftsman") == "Hello, Craftsman!"
        assert hello_solution.hello("Mr. X") == "Hello, Mr. X!"

    
