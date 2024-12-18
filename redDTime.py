### redDTime.py

#############################################################################################################
#
# --- redDTime ---
#
#   redDTime defines a class for date and time description in the form of @redD-taks'redD-tiks@ .
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

from datetime import datetime
from typing import Optional
import math

class redDTime:
    def __init__(self) :
        
        self.NULL_YEAR = 1990
        self.NULL_MONTH = 11
        self.NULL_DAY = 12
        self.NULL_HOUR = 0
        self.NULL_MIN = 0
        self.NULL_SEC = 0
        
        rdt = "@00.00.00'00.000@"
    
    def calc_redDTime(self,
                      actYear : Optional[int] = 1990,
                      actMonth  : Optional[int] = 11,
                      actDay : Optional[int] = 12,
                      actHour : Optional[int] = 0,
                      actMin : Optional[int] = 0,
                      actSec : Optional[int] = 0,
                      actMicroSec : Optional[int] = 0) :
        """calculates the redDTime."""
        redDtiks = str(round((actHour * 60 * 60 + actMin * 60 + actSec) / 0.864) / 1000)

        if (redDtiks.index(".") == 1 or len(redDtiks) == 1) :
            redDtiks = "0" + redDtiks 
        if (len(redDtiks) <= 5) :
            if (len(redDtiks) == 2) :
                redDtiks = redDtiks + "." 
            for i in range(len(redDtiks), 5) :
                redDtiks = redDtiks + "0" 

        xYear = actYear - self.NULL_YEAR
     
        actDate = datetime(actYear, (actMonth), actDay)
        refDate = datetime(actYear, (self.NULL_MONTH), self.NULL_DAY)

        diff = actDate - refDate
        
        if (diff.days < 0) :
            refDate1 = datetime((actYear - 1), (self.NULL_MONTH), self.NULL_DAY)
            diff = actDate - refDate1
            xYear = xYear - 1

        xDay = diff.days
        xMonth = math.floor(xDay / 28)

        if (xMonth > 12) : 
            xMonth = 12
        
        xDay = xDay - (xMonth * 28)
        redDtaks = str(xYear) + "." + "%02d" % xMonth + "." + "%02d" % xDay
        self.rdt = "@" + redDtaks + "'" + redDtiks + "@"
        
        return self.rdt
        
    def get_redDTime(self) :
        """get the redDTime."""
        # read current date
        actDT = datetime.now()
        actYear = actDT.year
        actMonth = actDT.month
        actDay = actDT.day
        actHour = actDT.hour
        actMin = actDT.minute
        actSec = actDT.second
        actMicroSec = actDT.microsecond

        return self.calc_redDTime(actYear, actMonth, actDay, actHour, actMin, actSec, actMicroSec)
        
    def set_redDTime(self, 
                     setYear : Optional[int] = 1990, 
                     setMonth  : Optional[int] = 11, 
                     setDay : Optional[int] = 12, 
                     setHour : Optional[int] = 0, 
                     setMin : Optional[int] = 0, 
                     setSec : Optional[int] = 0, 
                     setMicroSec : Optional[int] = 0) :
        """set the redDTime."""
        actYear = setYear
        actMonth = setMonth
        actDay = setDay
        actHour = setHour
        actMin = setMin
        actSec = setSec
        actMicroSec = setMicroSec

        return self.calc_redDTime(actYear, actMonth, actDay, actHour, actMin, actSec, actMicroSec)
    
    def __str__(self):
        return f"redDTime defines a class for date and time description and handling in the form of @redD-taks'redD-tiks@ ."