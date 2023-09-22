import polars as pl
import datetime
import jdatetime
import math


def convert_date(date):
    return jdatetime.date.fromgregorian(date=date)


def jdate(date):
    return convert_date(date).strftime("%Y-%m-%d")


def jweek_day(date):
    return convert_date(date).weekday()


def jweek_number(date):
    return convert_date(date).weeknumber()


def jyear(date):
    return convert_date(date).year


def jmonth(date):
    return convert_date(date).month


def jquarter(month):
    return math.ceil(month / 3)


def jday(date):
    return jdatetime.date.fromgregorian(date=date).day


def df_date():
    df = pl.DataFrame(
        pl.date_range(
            start=datetime.date(year=2001, month=1, day=1),
            end=datetime.date(year=2030, month=1, day=1),
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
