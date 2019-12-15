import datetime
import pytz

utc = pytz.timezone('UTC')

dt_aware = datetime.datetime(2019, 1, 1, 1, 0, 30, 1000,
                             tzinfo=datetime.timezone.utc)

aware_date = utc.localize(dt_aware)


