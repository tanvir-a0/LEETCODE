import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        years, months, days = date.split("-")
        year = int(years)
        month = int(months)
        day = int(days)
        dtm = datetime.datetime(year, month, day)

        return dtm.timetuple().tm_yday
        
