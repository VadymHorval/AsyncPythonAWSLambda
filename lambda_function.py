import asyncio
import json
import urllib3
import collections

TABLE_ID = 'app3DEEwui4OTkeDI'
API_KEY = 'keywRoiRn61Sk3nvo'
TABLE_NAME = 'MainTable'
print_list = ''
count = 0

def lambda_handler(event, context):
    asyncio.run(main())
    response = {
        "statusCode": 200,
        "body": print_list
    }
    return response

async def main():
    global print_list
    global count
    table_url = f'https://api.airtable.com/v0/{TABLE_ID}/{TABLE_NAME}?fields%5B%5D=ID&fields%5B%5D=title'
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    http = urllib3.PoolManager()
    r = http.request('GET',url=table_url, headers=HEADERS)  # get data
    data = json.loads(r.data.decode("utf-8"))
    r_buffer = collections.deque(maxlen=len(data['records']))  # create a ring buffer

    for i in data['records']:  # init buffer
        r_buffer.append(i['fields'].get('title'))

    r_buffer.rotate(count) #scroll the buffer
    count += 1
    print_list += ('|' + r_buffer[0] + '->' + r_buffer[1] + '->' + r_buffer[2] + '|::')