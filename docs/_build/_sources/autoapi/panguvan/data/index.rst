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




.. py:class:: ISE(daily_hist_price: bool = True, daily_adj_hist_price: bool = True, intraday_trades: bool = True)


   Get Iran Stock Exchange data and update them.

   .. py:method:: write_date_table()


   .. py:method:: write_trbc_tables(trbc_hdf_path: str) -> None

      Append The Refinitiv Business Classification data to tables.
      :param trbc_hdf_path: TRBC.h5 file path. You can download hear: SO_.
                            .. _SO: https://github.com/yghaderi/panguvan
      :type trbc_hdf_path: str


   .. py:method:: write_market_table(id: List[int] = [1, 2, 3], name: List[str] = ['tse', 'ifb', 'ifb-otc'])


   .. py:method:: get_last_update_date(table)


   .. py:method:: handle_update_date(table)


   .. py:method:: update_daily_hist_price(instruments: List[Tuple[str, int]])

      Get hist-price and push on table.
      :param instruments:
      :type instruments: List[Tuple[str, int]], [(ins_id, ins_code), ...]


   .. py:method:: update_daily_adj_hist_price()



