import pytest

from pom.buyturkeytickets import BuyPopularTurkeyTickets


@pytest.mark.usefixtures('setup')
class TestHomePage:
    def test_anyway(self):
        tickets_anyway = BuyPopularTurkeyTickets(self.driver)
        tickets_anyway.go_to_buy_tickets()
