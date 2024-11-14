import requests
import urllib.parse
from datetime import datetime
from wbi import encWbi, getWbiKeys
import uuid
from prettytable import PrettyTable

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0'


def api_request(
    url: str,
    params: dict,
    sessdata: str,
    referer: str = 'https://www.bilibili.com/'
) -> dict:
    img_key, sub_key = getWbiKeys()
    params['platform'] = 'web'
    signed_params = encWbi(params, img_key, sub_key)
    query = urllib.parse.urlencode(signed_params)
    headers = {
        'cookie': f'SESSDATA={sessdata}; buvid3={str(uuid.uuid1()).upper()}; bili_jct=4b3b3b3b3b3b3b3b3b3b; buvid4={str(uuid.uuid1()).upper()}',
        # buvid3 为无意义随机值
        'User-Agent': USER_AGENT,
        'Referer': referer,
    }
    resp = requests.get(url, params=query, headers=headers)
    # print(resp.text)
    return resp.json()


def readable(num: int) -> str:
    if num < 1e4:
        return str(num)
    elif num < 1e8:
        return f"{num / 1e4:.1f} 万"
    else:
        return f"{num / 1e8:.1f} 亿"


def readable_date(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


def main():
    sessdata = input("输入 SESSDATA：")
    uid = 15135791

    # 基本信息
    user_info = api_request(
        'https://api.bilibili.com/x/space/wbi/acc/info',
        {'mid': uid, 'token': ''}, sessdata
    )
    print(f"UP 主：{user_info['data']['name']}\t", end='')

    user_card = api_request(
        'https://api.bilibili.com/x/web-interface/card',
        {'mid': uid, 'token': '', 'photo': False}, sessdata
    )
    print('粉丝数', user_card['data']['follower'])

    table = PrettyTable(['标题', '播放量', '发布日期', '链接（点击观看）'])
    
    # 视频
    search_result = api_request(
        'https://api.bilibili.com/x/space/wbi/arc/search',
        {
            'mid': uid,
            'pn': 1,
            'ps': 30,
            'index': 1,
            'order': 'pubdate',
            'order_avoided': True,
            'tid': 0,
        },
        sessdata,
        referer=f'https://space.bilibili.com/{uid}/video'
    )

    for video in search_result['data']['list']['vlist']:
        link = f"\x1b]8;;https://www.bilibili.com/video/{video['bvid']}\x1b\\{video['bvid']}\x1b]8;;\x1b\\"
        if video['meta'] is not None:
            table.add_row([
                f"{video['meta']['title']} [共{video['meta']['ep_count']}集]",
                readable(video['meta']['stat']['view']),
                readable_date(video['created']),
                link
            ])
        else:
            table.add_row([
                video['title'],
                readable(video['play']),
                readable_date(video['created']),
                link
            ])
    
    print(table)


if __name__ == '__main__':
    main()
