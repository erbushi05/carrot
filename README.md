# Source Code




## File Illustration

```text
.
├── README.md
├── img1.png
├── main.py
├── template
│   └── README.md # 模板
├── url_check.ipynb # 一个检查url的脚本
└── utils # 一些工具方法
    ├── __init__.py
    ├── data.py
    ├── jinja.py
    └── url_check.py


```



##  Rank

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

```python
def sort_site(items, gfw=True):
    items = sorted(items, key=lambda x: x.weight, reverse=True)
    if gfw:
        items_g = [x for x in items if x.gfw == 1]
        items_g.extend([x for x in items if x.gfw != 1])
        items = items_g
    return items

```

### ~~GitHubAction Auto sync(弃用)~~

> GitHubAction每十分钟自动同步 dev 分支[README.md](https://github.com/xx025/carrot/blob/dev/README.md)
> 请开起Action 可读写仓库
>
> 开启方法：
> 1. Actions permissions -->[✔]Allow all actions and reusable workflows # 允许action运行
> 2. Workflow permissions-->[✔]Read and write permissions # 给与action读写权限

```yml
name: Sync
on:
  schedule:
    - cron: '*/10 * * * *'
jobs:
  sync-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        with:
          ref: main # 要同步的分支
      - name: Download README.md
        run: |
          curl  -o README.md https://raw.githubusercontent.com/xx025/carrot/main/README.md
          echo "$(cat README.md)"$'\n\n>Last synced:BeiJingT '"$(TZ='Asia/Shanghai' date +'%Y-%m-%d %H:%M:%S')" > README.md
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16.x'
      - name: Set up Git user
        run: |
          git config --global user.email "actions@github.com"
          git config --global user.name "GitHub Actions"
      - name: Check if changes exist
        run: |
          if git diff-index --quiet HEAD --; then
            echo "No changes to commit. Exiting."
          else
            git add README.md
            git commit -m "Sync README to main branch"
            git push origin HEAD:refs/heads/main
          fi
```




## Star History

![star-history](https://api.star-history.com/svg?repos=xx025/carrot&type=Timeline)

