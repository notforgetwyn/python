import re
import os

i_month_table = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
str_week_table = ["星期五", "星期六", "星期天", "星期一", "星期二", "星期三", "星期四"]
BASEYEAR = 1582
BASEMONTH = 10
BASEDAY = 15
LEAPDAY = 29
NONLEAPDAY = 28
YEAR = 365


def countLeap(i_start, i_end):
    sum = 0
    j = 0
    if (i_end > BASEYEAR):
        j = 1
    for i in range(i_start, i_end + j, 1):
        if (isLeap(i_start)):
            sum += 1
        i_start += 1
    return sum


def isLeap(i_year):
    if i_year % 4 == 0 and i_year % 100 != 0 or (i_year % 400 == 0) and i_year > BASEYEAR:
        return True
    elif (i_year % 4 == 0) and i_year < BASEYEAR:
        return True
    else:
        return False


def isdate(str_date):
    if (len(str_date) != 8):
        return False
    str_reyear = "[0-9]{4}"
    str_remonth = "(0[1-9])|(1[0-2])"
    str_reday = "(0[1-9])|([1-2][0-9])|(3[0-1])"
    str_year = str_date[:4]
    str_month = str_date[4:6]
    str_day = str_date[6:8]
    i_year = int(str_year)
    i_month = int(str_month)
    i_day = int(str_day)
    if ((re.match(str_reyear, str_year))
            and (re.match(str_remonth, str_month))
            and (re.match(str_reday, str_day))):
        if (i_month == 2):
            if (isLeap(i_year)):
                if (i_day > LEAPDAY):
                    return False
            elif (i_day > NONLEAPDAY):
                return False
        elif (i_month_table[i_month - 1] < i_day):
            return False
    else:
        return False
    if (i_year == BASEYEAR and i_month == BASEMONTH and i_day in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]):
        return False
    return True


def computeDate(str_date):
    i_year = int(str_date[:4])
    i_month = int(str_date[4:6])
    i_day = int(str_date[6:8])
    i_Dvalue = i_year - BASEYEAR
    i_result = i_day - BASEDAY
    i_delta = abs(i_month - BASEMONTH)
    if (i_month > BASEMONTH):
        for i in range(0, i_delta, 1):
            i_result += i_month_table[BASEMONTH - 1 + i]
    elif (i_month < BASEMONTH):
        for i in range(0, i_delta, 1):
            i_result -= i_month_table[BASEMONTH - 2 - i]
            if (i == 7):
                if (isLeap(i_year)):
                    i_result -= LEAPDAY
                else:
                    i_result -= NONLEAPDAY
    if (i_year < BASEYEAR or (i_year == BASEYEAR and i_month < BASEMONTH) or (
            i_year == BASEYEAR and i_month == BASEMONTH and i_day < BASEDAY)):
        if (i_year < (BASEYEAR - 2)):
            i_DvalueHasLeap = (-i_Dvalue) - 2
            if (i_year % 100 == 0):
                i_result += i_Dvalue * YEAR - (int(i_DvalueHasLeap / 4 - 1)) + 3 * int(
                    (int((i_DvalueHasLeap) / 100) * 100 / 400)) + int(
                    (int((i_DvalueHasLeap) / 100) * 100 % 400 / 100)) - 1
            elif (i_year % 4 == 0):
                i_result += i_Dvalue * YEAR - (int(i_DvalueHasLeap / 4 - 1)) + 3 * int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 / 400)) + int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 % 400 / 100)) - 1
            else:
                i_result += i_Dvalue * YEAR - (int(i_DvalueHasLeap / 4)) + 3 * int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 / 400)) + int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 % 400 / 100)) - 1
        else:
            i_result += i_Dvalue * YEAR
        return (-i_result)
    else:
        if (i_year > (BASEYEAR + 18)):
            i_DvalueHasLeap = i_Dvalue - 18
            i_result += i_Dvalue * YEAR + (int(i_DvalueHasLeap / 4)) - 3 * int(
                (int(i_DvalueHasLeap / 100) * 100 / 400)) - int((int(i_DvalueHasLeap / 100) * 100 % 400 / 100)) + 5
        else:
            i_result += i_Dvalue * YEAR + countLeap(BASEYEAR, i_year)
        return i_result


def grafhUserInterface():
    print("********日期查找******** ")
    print("----------------------------------")
    print("----------------------------------")
    print("--输入1进入闰年判断--")
    print("--输入2进入星期数判断--")
    print("--输入3进入两个日期数差计算--")
    print("--输入0结束程序------------")
    print("---------请输入数字----------")


while (1):
    grafhUserInterface()
    num = input()
    if (num == "0"):
        exit()
    elif (num == "1"):
        print("-------------输入要判断的年份格式为yyyymmdd---------------------")
        print("-------------例如20181010代表2018年10月10日---------------------")
        yymmdd_date = input()
        if (isdate(yymmdd_date)):
            if (isLeap(int(yymmdd_date[0:4]))):
                print(yymmdd_date + "是闰年")
            else:
                print(yymmdd_date + "不是闰年")
        else:
            print("请输入正确的格式")
            print("输入1表示重新输入")
            print("输入2表示返回主菜单")
            print()
    elif (num == "2"):
        pass
    elif (num == "3"):
        pass
