#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
pandas 使用
"""
# 导入包
import numpy as np
import pandas as pd



class DownloadData():
    """
    加载数据
    """

    def to_list(self):
        """

        :return:
        """
        df_list = pd.DataFrame([[np.nan, 2, np.nan, 0, 'asd'],
                                [3, 4, np.nan, 1, 'ddd'],
                                [np.nan, np.nan, np.nan, 5, 'asl'],
                                [np.nan, 3, np.nan, 4, 'aec']],
                               columns=list('ABCDE'))

    def to_csv(self):
        """

        :return:
        """
        df_csv = pd.read_csv()

    def to_mysql(self):
        """

        :return:
        """
        df_mysql = pd.read_sql()


class DataManipulation():
    """
    数据操作
    """

    def column(self, df):
        """

        :param df:
        :return:
        """
        cl = list('ACBDEF')
        df = df.reindex(columns=cl, fill_value=0)

    def columns(self, df):
        """

        :param df:
        :return:
        """
        cl = list('ACBDEF')

        df = df.reindex(columns=cl, fill_value=0)

    # dataframe 合并

    # 改变 dataframe


class DataManipulationSql():
    """
    dataframe 类似SQL操作
    """

    def _sqlLike(self, df):
        """

        :param df:
        :return:
        """
        df.loc[~df.E.str.startswith('as')]


if __name__ == '__main__':
    print('--')
