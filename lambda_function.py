import asyncio
import json
import urllib3
import collections

TABLE_ID = 'app3DEEwui4OTkeDI'
API_KEY = 'keywRoiRn61Sk3nvo'
TABLE_NAME = 'MainTable'
print_list = []
count = 0

def lambda_handler(event, context):
    str_count = ''

    for n in event["rawQueryString"]:
        if n.isdigit():
            str_count += n
    count = int(str_count)

    asyncio.run(main())
    #r_str = (' '.join(str(e) for e in print_list)) +"!!!!!!!!!!!!!ID:" + event["rawQueryString"] +":::Event:"+ json.dumps(event)
    r_str = (' '.join(str(e) for e in print_list)) + "!!!!!!!!!!!!!ID:" + event["rawQueryString"]

    response = {
        "statusCode": 200,
        "body": r_str
    }
    return response

async def main():
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

    r_buffer.rotate(count)
    print_list.append('|' + r_buffer[0] + '->' + r_buffer[1] + '->' + r_buffer[2] + '|')

