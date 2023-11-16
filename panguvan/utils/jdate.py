import polars as pl
import datetime
import jdatetime
import math


def convert_date(date: datetime.date):
    """Convert date from gregorian to jalali.

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    jdatetime.date
    """
    return jdatetime.date.fromgregorian(date=date)


def jdate(date: datetime.date):
    """Convert date from gregorian to jalali and return jalali date string-format.

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    str
    """
    return convert_date(date).strftime("%Y-%m-%d")


def jweek_day(date: datetime.date):
    """Convert date from gregorian to jalali and return jalali week-day.

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    int
    """
    return convert_date(date).weekday()


def jweek_number(date: datetime.date):
    """Convert date from gregorian to jalali and return jalali week-number

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    int
    """
    return convert_date(date).weeknumber()


def jyear(date: datetime.date):
    """Convert date from gregorian to jalali and return jalali year.

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    int
    """
    return convert_date(date).year


def jmonth(date: datetime.date):
    """Convert date from gregorian to jalali and return jalali month.

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    int
    """
    return convert_date(date).month


def jquarter(month: int):
    """Convert date from gregorian to jalali and return jalali quarter.

    Parameters
    ----------
    month: int
        Month number.

    Returns
    -------
    int
    """
    return math.ceil(month / 3)


def jday(date: datetime.date):
    """Convert date from gregorian to jalali and return jalali day.

    Parameters
    ----------
    date: datetime.date
        Gregorian date.

    Returns
    -------
    int
    """
    return jdatetime.date.fromgregorian(date=date).day


def df_date(
    start: datetime.date,
    end: datetime.date,
):
    """
    Create polars.DataFrame from start date to end date whit columns:
        date: pl.Date
        jdate: pl.Utf8
        jweek_day:
        jweek_day:
        jweek_number:
        jyear
        jmonth
        jday
        jquarter:
        gregorian-date, Jalali-date, jalali week-day, jalali
    week-number,
    Parameters
    ----------
    start
    end

    Returns
    -------

    """
    df = pl.DataFrame(
        pl.date_range(
            start=start,
            end=end,
            interval="1d",
            eager=True,
        ).alias("date")
    )
    df = df.with_columns(
        pl.col("date").map_elements(jdate).alias("jdate"),
        pl.col("date").map_elements(jweek_day).alias("jweek_day"),
        pl.col("date").map_elements(jweek_number).alias("jweek_number"),
        pl.col("date").map_elements(jyear).alias("jyear"),
        pl.col("date").map_elements(jmonth).alias("jmonth"),
        pl.col("date").map_elements(jday).alias("jday"),
    )
    df = df.with_columns(pl.col("jmonth").map_elements(jquarter).alias("jquarter"))
    return df
