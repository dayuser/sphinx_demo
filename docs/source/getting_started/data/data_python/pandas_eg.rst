.. _data_python_pandas:

=========
pandas
=========


基本导入
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


列处理
^^^^^^^^

* 暴力改列名

.. ipython:: python

    df.columns=list('acdb')
    df

.. warning::

    不建议这样改列名

    * 要修改列名只俺能跟原dataframe列顺序依次修改（列的顺序是会有变化的，很有可能你修改列名会乱，除非在修改之前把dataframe列排序）

    * 要修改的列名`必须`和原dataframe的列数保持`一致`

* 指定列修改名

`rename`_ 更改列索引标签

.. ipython:: python

    df.rename(columns={'a':'a','c':'b','d':'c','b':'d','e':'e'},inplace=True)
    df

.. note::

    使用rname方法会很友善的修改列名 不至于列含义冲突， 修改不存在的列也不会报错

.. _fillna: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html?highlight=fillna#pandas.DataFrame.fillna
.. _rename: https://pandas.pydata.org/pandas-docs/version/1.1.0/reference/api/pandas.DataFrame.rename.html?highlight=rename#pandas.DataFrame.rename