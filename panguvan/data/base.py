import datetime
import asyncio
from panguvan.db import write_df
from panguvan.utils.jdate import df_date

loop = asyncio.get_event_loop()


def write_date_table(
    start: datetime.date = datetime.date(year=2001, month=1, day=1),
    end: datetime.date = datetime.date(year=2030, month=1, day=1),
):
    """
    .. raw:: html

        <div dir="rtl">
            جدولِ تاریخ رو از از تاریخِ ابتدا تا انتها پُر می‌کنه.
        </div>

    Parameters
    ---------
    start: datetime.date, default datetime.date(year=2001, month=1, day=1)
        تاریخِ ابتدا
    end: datetime.date, default datetime.date(year=2030, month=1, day=1)
        تاریخِ انتها
    """
    df = df_date(start=start, end=end)
    loop.run_until_complete(write_df(table="date", df=df))
    loop.close()
