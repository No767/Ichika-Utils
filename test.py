from ichika_utils import IchikaUtils
import asyncio
import uvloop
from pyinstrument import Profiler
import numpy as np
profiler = Profiler()

profiler.start()
async def main():
    
    data = np.random.randn(5000000)
    utils = IchikaUtils()
    print(await utils.graphHistoRandn(5000000))

    
    
   
    
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.run(main())
profiler.stop()
profiler.print()

