### redDTime_main.py

#############################################################################################################
#
# --- redDTime_main ---
#
#   redDTime defines a class for date and time description in the form of @redD-taks'redD-tiks@ .
#   redDTime_main shows the usage of redDTime.
#
# copyright: 
#   
#   (c) by Roland Degelmann, takatoa 
#   Mail : rode@takatoa.net
#   Web  : takatoa.net
#   
# created | last modified | version:
#
#   2024-12-01 | 2024-12-16 | version: 0.1.0
#
#############################################################################################################

from redDTime import redDTime

if __name__ == '__main__':
    rdt = redDTime()
    print("\n\nshow the usage of redDTime\n")
    print('***', rdt, '***\n')
    myRdt = rdt.get_redDTime()
    print("get actual redDTime\t:", myRdt)
    myRdt = rdt.set_redDTime(1993, 11, 11, 8, 15, 52, 37)
    print("set redDTime\t\t:", myRdt, "\t<-- Input data: '1993, 11, 11, 8, 15, 52, 37'")
    myRdt = rdt.set_redDTime(1897, 4)
    print("set redDTime\t\t:", myRdt, "\t<-- Input data: '1897, 4'")
