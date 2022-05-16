import asyncio
import pandas as pd
import numpy as np
import uvloop

class IchikaUtils:
    def __init__(self):
        self.self = self
        
    async def init(self):
        for _ in range(10):
            await asyncio.sleep(3)
            print("hello world")
    asyncio.set_event_loop_policy(uvloop.EventPolicy())            
    async def calcSummary(self):
        df_describe = pd.DataFrame({
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    })
        df_describe.describe()
