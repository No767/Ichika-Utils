from ichika_utils import IchikaUtils
import asyncio

async def main():
    utils = IchikaUtils()
    print(await utils.calcSummary())
    
asyncio.run(main())