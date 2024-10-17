from datetime import datetime
import re

i_month_table = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
str_week_table = ["星期五", "星期六", "星期天", "星期一", "星期二", "星期三", "星期四"]
BASEYEAR = 1582
BASEMONTH = 10
BASEDAY = 15
date1 = "15821015"


def isLeap(i_Year):
    if (i_Year % 4 == 0 and i_Year % 100 != 0) or (i_Year % 400 == 0):
        return True
    return False


def countLeap(i_start, i_end):
    sum = 0
    j = 0
    if (i_end > 1582):
        j = 1
    for i in range(i_start, i_end + j, 1):
        if (isLeap(i_start)):
            sum += 1
        i_start += 1
    return sum


def computeAfter1582(str_date):
    i_year = int(str_date[:4])
    i_month = int(str_date[4:6])
    i_day = int(str_date[6:8])
    i_Dvalue = i_year - BASEYEAR
    i_result = i_day - BASEDAY
    i_delta = abs(i_month - 10)
    if (i_month > 10):
        for i in range(0, i_delta, 1):
            i_result += i_month_table[BASEMONTH - 1 + i]
    elif (i_month < 10):
        for i in range(0, i_delta, 1):
            i_result -= i_month_table[BASEMONTH - 2 - i]
            if (i == 7):
                if (isLeap(i_year)):
                    i_result -= 29
                else:
                    i_result -= 28
    if (i_year < 1582 or (i_year == 1582 and i_month < 10) or (i_year == 1582 and i_month == 10 and i_day < 15)):
        if (i_year < 1580):
            i_DvalueHasLeap = (-i_Dvalue) - 2
            if (i_year % 100 == 0):
                i_result += i_Dvalue * 365 - (int(i_DvalueHasLeap / 4 - 1)) + 3 * int(
                    (int((i_DvalueHasLeap) / 100) * 100 / 400)) + int(
                    (int((i_DvalueHasLeap) / 100) * 100 % 400 / 100)) - 1
            elif (i_year % 4 == 0):
                i_result += i_Dvalue * 365 - (int(i_DvalueHasLeap / 4 - 1)) + 3 * int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 / 400)) + int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 % 400 / 100)) - 1
            else:
                i_result += i_Dvalue * 365 - (int(i_DvalueHasLeap / 4)) + 3 * int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 / 400)) + int(
                    (int((i_DvalueHasLeap + 20) / 100) * 100 % 400 / 100)) - 1
        else:
            i_result += i_Dvalue * 365
        return (-i_result)
    else:
        if (i_year > 1600):
            i_DvalueHasLeap = i_Dvalue - 18
            i_result += i_Dvalue * 365 + (int(i_DvalueHasLeap / 4)) - 3 * int(
                (int(i_DvalueHasLeap / 100) * 100 / 400)) - int((int(i_DvalueHasLeap / 100) * 100 % 400 / 100)) + 5
        else:
            i_result += i_Dvalue * 365 + countLeap(1582, i_year)
        return i_result


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
                if (i_day > 29):
                    return False
            elif (i_day > 28):
                return False
        elif (i_month_table[i_month - 1] < i_day):
            return False
    else:
        return False
    if (i_year == 1582 and i_month == 10 and i_day in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]):
        return False
    return True


def calculate_days_between_dates(date1, date2):
    """
    计算两个日期之间相差的天数。
    日期格式为 'yyyymmdd'。
    """
    # 将输入的日期字符串转换为日期对象
    try:
        d1 = datetime.strptime(date1, "%Y%m%d")
        d2 = datetime.strptime(date2, "%Y%m%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'yyyymmdd'.")

    # 计算日期差
    delta = abs((d2 - d1).days)
    return delta


# 输入两个日期
date2 = "00010101"

# print(calculate_days_between_dates(date1, "12001015"))
# print(computeAfter1582("12001015"))
for i in range(0, 15720005, 1):
    date2 = str(int(date2) + 1)
    while (len(date2) < 8):
        date2 = "0" + date2
    if (isdate(date2)):
     if (computeAfter1582(date2) != calculate_days_between_dates(date1, date2)):
        print(date2)

# try:
#     days_between = calculate_days_between_dates(date1, date2)
#     print(f"{date1} 和 {date2} 之间相差的天数是: {days_between} 天")
# except ValueError as e:
#     print(e)
