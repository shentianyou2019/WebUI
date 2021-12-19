# encoding=utf8
import pytest,os,time
import allure
from Config import setting
now = time.strftime("%Y-%m-%d %H_%M_%S")
reportfile = setting.TEST_REPORT + '/' + now + 'result.html'

def main():
    """运行pytest命令启动测试"""
    pytest.main(['--html=%s' % reportfile, '--self-contained-html'])
    # pytest.main(["--alluredir", "./Result/allure-results", ])
    # os.system(r"allure generate --clean ./Result/allure-results -o ./Result/allure-report")


if __name__ == '__main__':
    main()
