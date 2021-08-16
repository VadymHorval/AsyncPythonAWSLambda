import asyncio

# The AWS Lambda handler
import json


def lambda_handler(event, context):
    asyncio.run(main())
    return {
        "statusCode": 200,
        "body": json.dumps("Hello World")
    }

async def main():
    # Here you can await any awaitable
    await asyncio.sleep(1)
    print('Hello')
    await asyncio.sleep(1)
    print('World...')
