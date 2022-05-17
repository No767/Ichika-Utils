import asyncio
import numpy as np
import uvloop


class IchikaUtils:
    def __init__(self):
        self.self = self
        
    async def calcMean(self, array: np.array):
        a = np.array(array)
        return np.mean(a)
    
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    
    async def calcStats(self, array: np.array):
        npyArray = np.array(array)
        return {"mean": np.mean(npyArray), "median": np.median(npyArray), "std": np.std(npyArray), "variances": np.var(npyArray)
                , "spread": np.ptp(npyArray)}
    
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        
        
    
    
    
    
