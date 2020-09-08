.. _data_python_pandas:

************
pandas
************




基本导出
========
通常我们以一下方式导入:

.. ipython:: python

    import numpy as np
    import pandas as pd

数据处理
=========

nan 处理
^^^^^^^^
创建对象:

.. ipython:: python

    df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                       [3, 4, np.nan, 1],
                       [np.nan, np.nan, np.nan, 5],
                       [np.nan, 3, np.nan, 4]],
                      columns=list('ABCD'))
    df

方法fillna
----------

`fillna`_ 用于nan值填充

* 全部填充

.. ipython:: python

    df.fillna(0)

*  指定列填充

.. ipython:: python

    values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    df.fillna(value=values)

*  还可以向前或向后传播非null值。

.. ipython:: python

    df.fillna(method='backfill')
    df.fillna(method='bfill')
    df.fillna(method='pad')
    df.fillna(method='ffill')

.. _fillna: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html?highlight=fillna#pandas.DataFrame.fillna