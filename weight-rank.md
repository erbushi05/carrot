

####  排序
```python
    # 按权重排序
    # 权重 基本为 免费，登录，付费
    data1.extend(sort_site(data.free_star, gfw=False))
    data1.extend(sort_site(data.free))
    data1.extend(sort_site(data.deng_lu))
    data1.extend(sort_site(data.charge))
    # 打乱
    random.shuffle(data.miao_zhan)
```