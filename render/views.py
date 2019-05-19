from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    context = {
        'city': '成都',
        'adict': {
            'name': 'Alice',
            'age': 18
        },
        # 'alist': ['篮球', '游泳', '跑步']
        'alist': [],
        'age': 6,
        'time':datetime.now()
    }

    return render(request, 'index.html', context)


'''

比较运算符如下：
==
!=
<
>
<=
>=
布尔运算符如下：

and
or
not
注意：运算符左右两侧不能紧挨变量或常量，必须有空格。

'''


def filter(request):
    context = {
        'number': 10,
        'a': '',
        'b':12,
        'adict': {
            'name': 'Alice',
            'age': 18
        },
        'alist': ['篮球', '游泳', '跑步']
    }
    return render(request, 'filter的使用.html', context)


def jiaja(request):
    context = {
        'city': '成都',
        'adict': {
            'name': 'Alice',
            'age': 18
        },
        'alist': ['篮球', '游泳', '跑步'],
        # 'alist': [],
        'age': 6,
        'tim': datetime.now()
    }

    return render(request, 'jiaja2模板的使用.html', context)