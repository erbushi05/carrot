# -*- coding: UTF-8 -*-

def output_to_file(data, template_file, output_file, template_dir):
    """

    :param template_dir: 模板文件所在文件夹
    :param data: 要渲染的数据
    :param template_file: 模板文件夹
    :param output_file: 要输出的文件
    :return:
    """
    # 创建一个模板加载器，用于从文件中加载模板
    loader = FileSystemLoader(template_dir)

    # 创建一个环境对象，用于设置模板的选项和全局变量
    env = Environment(loader=loader)

    # 加载模板
    template_file = env.get_template(template_file)

    # 渲染数据
    result = template_file.render(data)

    # 写入文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)



def load_data():
    return dict()