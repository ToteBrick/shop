from jinja2 import Environment


def environment(**options):
    env = Environment(**options)

    # 将定义的过滤器添加到环境中
    env.filters['sum']= sum
    env.filters['date']= date

    return env


# 1.定义过滤器
def sum(x):
    return x + x

# 自定义时间过滤器
from datetime import datetime
def date(timeparam):
    return datetime.strftime(timeparam, '%Y%m%d')

