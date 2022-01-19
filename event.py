
class Event:
    def __init__(self, name, location, price, organiser, date):
        self.name = name
        self.location = location
        self.price = price
        self.organiser = organiser
        self.date = date

    def eventName(self):
        return("This event is called: " + self.name)

    def eventLocation(self):
        return("This location is called: " + self.location)

    def eventPrice(self):
        return("This price for this event is: " + self.price)

    def eventOrganiser(self):
        return("The organiser of the event is: " + self.organiser)



firstEvent = Event(
    "First Party", "Croydon", "10", "OfficialKush", "15/12/2021"
)


class HipHopEvent(Event):
    pass


class DayParty(Event):
    pass


class Rave(Event):
    pass


class HouseParty(Event):
    pass


class Birthday(Event):
    pass

class Concert(Event):
    pass

firstHipHopEvent = HipHopEvent(
    "First Hiphop Event", "Croydon", "20", "CDP", "15/12/2021")

print(firstHipHopEvent.eventName())
print(firstHipHopEvent.eventLocation())
