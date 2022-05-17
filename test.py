from ichika_utils import IchikaUtils
import asyncio
import uvloop
from pyinstrument import Profiler
profiler = Profiler()

profiler.start()
async def main():
    
    data = [1, 3, 4, 5, 7, 9, 2]
    utils = IchikaUtils()
    print(await utils.calcStats(data))

    
    
   
    
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.run(main())
profiler.stop()
profiler.print()

