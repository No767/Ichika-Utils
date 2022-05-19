from ichika_utils import IchikaUtils, StandardDeviationCalc, LinRegression
import asyncio
import uvloop
from pyinstrument import Profiler
import numpy as np
profiler = Profiler()

profiler.start()
async def main():
    
    data = np.random.randn(5000000)
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_data_list = [2, 4, 6, 3, 6, 3, 6,2, 6,2 ]
    linRegressionUtils = LinRegression()
    print(await linRegressionUtils.calcLinRegressionX(x_data=data_list, y_data=y_data_list))
    
    
   
    
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.run(main())
profiler.stop()
profiler.print()

