from jinja2 import Environment


def environment(**options):
    env = Environment(**options)

    # 将定义的过滤器添加到环境中
    env.filters['sum']= sum

    return env


# 1.定义过滤器
def sum(x):
    return x + x
