:py:mod:`panguvan.data`
=======================

.. py:module:: panguvan.data


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   ise/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   panguvan.data.ISE




.. py:class:: ISE(daily_hist_price: bool = True, daily_adj_hist_price: bool = True, intraday_trades: bool = False)


   Get **Iran Stock Exchange** data and update them by https://github.com/yghaderi/oxtapus.

   :param daily_hist_price: if ``True`` the **daily-hist-price** of all stocks that are listed will be updated. Default: ``True``
   :type daily_hist_price: bool
   :param daily_adj_hist_price: if ``True`` the **adjusted-daily-hist-price** of all stocks that are listed will be updated. Default: ``True``
   :type daily_adj_hist_price: bool
   :param intraday-trades: if ``True`` the **intraday-trades** of the current day of all stocks that are listed will be updated. Default: ``False``
   :type intraday-trades: bool

   .. py:method:: write_date_table()


   .. py:method:: write_trbc_tables(trbc_hdf_path: str) -> None

      Append The Refinitiv Business Classification data to tables.
      :param trbc_hdf_path: TRBC.h5 file path. You can download this file `here`_.
                            .. _here: https://github.com/yghaderi/panguvan/blob/master/TRBC.h5
      :type trbc_hdf_path: str


   .. py:method:: write_market_table(id: List[int] = [1, 2, 3], name: List[str] = ['tse', 'ifb', 'ifb-otc'])


   .. py:method:: get_last_update_date(table)


   .. py:method:: handle_update_date(table)


   .. py:method:: update_daily_hist_price(instruments: List[Tuple[str, int]])

      Get hist-price and push on table.
      :param instruments:
      :type instruments: List[Tuple[str, int]], [(ins_id, ins_code), ...]


   .. py:method:: update_daily_adj_hist_price()



