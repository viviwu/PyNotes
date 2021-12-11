# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         date_time
# Description:
# Author:       Administrator
# Date:         2021/12/9
# desc: Copyright © Administrator All rights reserved.
# -------------------------------------------------------------------------------

import sys
from datetime import datetime,timedelta,time

dt_str = '2019-5-1 5:54:45'
day = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
print(day, type(day))

now = datetime.now()
dtstr=datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
print(dtstr, type(dtstr))

new_dt = now + timedelta(days=2, hours=12)
print(new_dt)