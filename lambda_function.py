"""Get data from URL
Initializes the rings buffer data.
Generates data for output from the ring buffer.
Outputs data using lambda AWS and AWS API Gateway
"""
import asyncio
import json
import collections
import urllib3


TABLE_ID = 'app3DEEwui4OTkeDI'
API_KEY = 'keywRoiRn61Sk3nvo'
TABLE_NAME = 'MainTable'
PRINT_LIST = ''
COUNT = 0


def lambda_handler(event, context):
    """ Lambdas handler method."""
    asyncio.run(main())
    response = {
        "statusCode": 200,
        "body": PRINT_LIST
    }
    return response

async def main():
    """ Generates data for output from the ring buffer. Initializes the data buffer from the URL"""
    global PRINT_LIST
    global COUNT
    table_url = f'https://api.airtable.com/v0/{TABLE_ID}/' \
                f'{TABLE_NAME}?fields%5B%5D=ID&fields%5B%5D=title'
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    http = urllib3.PoolManager()
    req = http.request('GET',url=table_url, headers=headers)  # get data
    data = json.loads(req.data.decode("utf-8"))
    r_buffer = collections.deque(maxlen=len(data['records']))  # create a ring buffer

    for i in data['records']:  # init buffer
        r_buffer.append(i['fields'].get('title'))

    r_buffer.rotate(COUNT) #scroll the buffer
    COUNT += 1
    PRINT_LIST += ('|' + r_buffer[0] + '->' + r_buffer[1] + '->' + r_buffer[2] + '|::')
