# -*- coding: UTF-8 -*-
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
    ,
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"'
}


def check_url(url, proxies=None) -> (int, str):
    if proxies is None:
        proxies = proxies
    try:
        response = requests.get(url, timeout=3, headers=headers)

        if response.status_code == 200:
            print('网站可以正常访问', url)
            return 1, '成功'
        else:
            return response.status_code, '非代理，失败'

    except requests.exceptions.RequestException as e:
        if proxies is not None:

            try:
                response = requests.get(url, proxies=proxies, timeout=3, headers=headers)
                if response.status_code == 200:
                    return 2, '代理，成功'
                else:
                    return response.status_code, '代理，失败'
            except requests.exceptions.RequestException as e:
                return 0, '代理,异常失败'

    return 0, '全异常'
