from django import template

register = template.Library()  # 实例化对象

'''
  创建一个template能认识的函数
  对创建的每一个过滤器，都要用加上装饰器
'''

@register.filter
def sum(a):
    return a + a