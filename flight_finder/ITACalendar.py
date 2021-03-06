__author__ = 'Brad Herrmann'

"""
Handles the calendar data received from ITA
"""
class ITACalendar:
    def __init__(self, data):
        self.data = data

    def get_lowest_price(self):
        return self.data["result"]["currencyNotice"]["ext"]["price"]

    def get_session_id(self):
        return self.data["result"]["session"]

    """
    finds the cheapest round trip
    returns a list containing the days leaving and the days returning for each
    pair matching the cheapest round trip. The days are in string format
    """
    def find_cheapest_rt(self):
        cheapest_dates = []
        calendar = ""
        try:
            calendar = self.data["result"]["calendar"]
        except KeyError:
                print "Error. No results"
                return cheapest_dates
        minPrice = self.get_lowest_price()
        for month in calendar["months"]:
            year = month["year"]
            the_month = month["month"]
            day_num = 1
            for week in month["weeks"]:
                for day in week["days"]:
                    date = day["date"]

                    #exclude dates in the week not in the current month. ie. exclude 6/30 in
                    # Monday 6/30, Tuesday 7/1, Wednesday 7/2, etc since 6/30 is not in July
                    if date != day_num:
                        continue
                    day_num = day_num+1
                    price = day.get("minPrice")
                    if price == minPrice:
                        outbound = str(year) + "-" + str(the_month) + "-" + str(date)
                        for trip in day["tripDuration"]["options"]:
                            #found a day with the cheapest price
                            if minPrice == trip["minPrice"]:
                                dates = []
                                dates.append(outbound) #append the leaving date
                                arrival = trip["solution"]["itinerary"]["arrival"]
                                arrival = arrival[:10] #strip off the time
                                dates.append(arrival) #append the returning date
                                cheapest_dates.append(dates)
        return cheapest_dates