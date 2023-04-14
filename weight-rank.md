

####  排序
```python
data1.extend(sort_site(data.free_star))  # 按权重排序
data1.extend(data.free)  # 不做排序
data1.extend(data.deng_lu)  # 不做排序
random.shuffle(data.charge)  # 打乱
data1.extend(sort_site(data.charge))

return data1
```