import Sail
from datetime import date


class Condition(Sail):              #CLASS NOT USED! Keep and idea for future!

    def giveCondition(self, sail):
        if sail.firstDate < date.today():
            self.condition = "USED"
        else:
            self.condition = "NEW"
