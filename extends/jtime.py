from . import jalali
from django.utils import timezone

def persian_number_convertor(my_str):
    numbers = {
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
    }

    for e, p in numbers.items():
        my_str =  my_str.replace(e, p)
    
    return my_str

def day_to_persian(list):
    days = [
        "یکم",
        "دوم",
        "سوم",
        "چهام",
        "پنجم",
        "ششم",
        "هفتم",
        "هشتم",
        "نهم",
        "دهم",
        "یازدهم",
        "دوازدهم",
        "سیزدهم",
        "چهاردهم",
        "پانزدهم",
        "شانزدهم",
        "هفدهم",
        "هجدهم",
        "نوزدهم",
        "بیستم",
        "بیست و یکم",
        "بیستم و دوم",
        "بیستم و سوم",
        "بیستم و چهارم",
        "بیستم و پنجم",
        "بیستم و ششم",
        "بیستم و هفتم",
        "بیستم و هشتم",
        "بیستم و نه ام",
        "سی ام",
        "سی و یکم",
        ]

    for index, day in enumerate(days):
        if list[2] == index + 1:
            list[2] = day
            break
    
    return list

def jalali_convertor(time):
    jmonth = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن"
    ]
    time = timezone.localtime(time)

    s_time = "{},{},{}".format(time.year, time.month, time.day)
    jalali_time = jalali.Gregorian(s_time).persian_tuple()
    time_to_list = list(jalali_time)

    for index, month in enumerate(jmonth):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break
    
    time_to_list = day_to_persian(time_to_list)

    output = "{} {} {}،ساعت {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
        
    )

    

    return persian_number_convertor(output)