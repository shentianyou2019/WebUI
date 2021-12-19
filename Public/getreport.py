#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os,sys
from Config import setting

report=setting.TEST_REPORT

def get_report(report):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(report)
    lists.sort(key=lambda fn: os.path.getmtime(report + "\\" + fn))
    file_new = os.path.join(report,lists[-1])
    return file_new