# Task 5

@Author: 斩风千雪   
@Email: me@chyk.ink

使用 requests 库爬取 B 站用户视频并输出，使用 prettytable 在终端输出表格，使用 ANSI 超链接转义序列输出可点击的链接。

B 站网页端会对用户的请求进行 wbi 签名校验，因此需要对请求进行签名。

API 文档和 wbi 签名算法：[bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)