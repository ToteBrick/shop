from django.shortcuts import render


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
        'age':6
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
