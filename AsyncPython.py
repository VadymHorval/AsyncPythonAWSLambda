import asyncio

# The AWS Lambda handler
def lambda_handler(event, context):
    asyncio.run(main())

async def main():
    # Here you can await any awaitable
    await asyncio.sleep(1)
    print('Hello')
    await asyncio.sleep(1)
    print('World..')