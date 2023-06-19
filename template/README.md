# Free ChatGPT Site List

**这儿为你准备了众多免费好用的ChatGPT镜像站点**

发布网站： [{{publish_site_url}} ]({{publish_site_url}}) 😃敬请收藏和分享

**分享站点**、**站点失效**、**标注错误**，请[🌺点此🌺]({{github_repo_url}}/issues)

----

<a href="{{ ad.redirect_url }}" target="_blank" style="color: black">
<img src="{{ ad.img }}" alt="Ad" style="height: 80px !important;width: auto !important;" ></a>
<br>
<a href="{{ ad.redirect_url }}" target="_blank" style="color: black">
👆 {{ ad.url }} [广告]
</a>

----

**标注说明**

| 🔖 | 📓        |
|----|-----------|
| ⭐  | 使用稳定，推荐   |
| 🆕 | 最近更新      |
| 😄 | 免费使用      |
| 🔑 | 需要登陆或密码   |
| ✈️ | 需国际网络进行访问 |

[//]: # (| 🤑 | 付费使用      |)

[//]: # (| 🎁 | 付费使用，体验次数 |)




{% for SITE in SITES %}

### {{SITE.class_name}}

{% if SITE.describe %}
> {{ SITE.describe }}
> {% endif %}

<table>
{% for item in SITE.datas %}
  <tr>
    <td>{{item.index}}.</td>
    <td><img src="{{item.favicon}}" alt="favicon" style="height: 20px !important;width: 20px !important;" ></td>
    <td><a href="{{item.url }}" target="_blank"> {{item.domain}} </a> </td>
    <td>{{item.content}}</td>
    <td>{{item.note}}</td> 
    <td><a href="{{item.url }}" target="_blank">🔗 </a> </td> 
  </tr>
{% endfor %}
</table>
{% endfor %}


#### 失效站点

<details>
  <summary>失效站点</summary>

{% for item in items_shi_xiao %}
{{item.index}}. {{ item.url }} <br/>
{% endfor %}

</details>

---

[GitHub]({{github_repo_url}})| [OSS]({{github_repo_url}}/tree/dev) | [站点提交]({{github_repo_url}}/issues/new/choose) | [站点反馈]({{github_repo_url}}/issues/new/choose) | [广告投放]({{publish_site_url}}/ads)

如果您正在同步或转载本仓库内容，请遵守以下协议：1. 可以移除广告位 2. 其他部分请保持原文，不作修改

> 最后更新: {{ timestamp }}
