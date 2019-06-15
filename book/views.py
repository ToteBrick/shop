import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import date

from django.views import View

from book.models import BookInfo, HeroInfo

# Create your views here.

# 增加操作
from book.serializers import BookSerializer


def info(request):
    book = BookInfo(btitle='西游记', bpub_date=date(1984, 3, 15), bread=21, bcomment=22)  # 增加
    book.save()  # 保存进数据库
    allbook = BookInfo.objects.all()  # 查询表里所有内容
    print(allbook)
    hero = HeroInfo.objects.create(hname='沙和尚', hgender=0, hbook=book)  # 增加的另一种方式
    hero.save()
    all_hero = HeroInfo.objects.all()
    print(all_hero)
    # a_list = []
    # a_dict = dict()
    # for one in allbook:
    #     a_dict['btitle'] = one
    #     a_list.append(a_dict)
    context = {
        # 'book':a_list
    }
    # print(context)
    return render(request, 'model.html', context=context)


# 删除操作
def delete(request):
    book = BookInfo.objects.get(id=7)
    book.delete()  # 删除的第一种方式
    HeroInfo.objects.filter(id=14).delete()  # 删除的第二种方式
    return HttpResponse('delete option')


# 修改操作
def update(request):
    # hero = HeroInfo.objects.get(hname='沙和尚')
    # hero.hname = '沙悟净'
    # hero.hcomment = '沙和尚'
    # hero.save()
    HeroInfo.objects.filter(hname='胡斐').update(hname='胡一刀')  # 修改的第二种方式
    return HttpResponse('update option')


def query(request):
    # 查询编号为1的图书
    print(BookInfo.objects.filter(id=1))
    # contains：是否包含，查询书名包含'传'的图书
    print(BookInfo.objects.filter(btitle__contains='传'))
    # 查询阅读量大于等于评论量的图书
    # startswith、endswith：以指定值开头或结尾
    print(BookInfo.objects.filter(btitle__endswith='部'))
    # 查询书名不为空的图书
    print(BookInfo.objects.filter(btitle__isnull=False))
    # in ：是否包含在范围内,查询编号为1或3或5的图书
    print(BookInfo.objects.filter(id__in=[1, 3, 5]))
    '''
比较查询
gt 大于 (greater then)
gte 大于等于 (greater then equal)
lt 小于 (less then)
lte 小于等于 (less then equal)
    '''
    # 查询编号大于3的图书
    print(BookInfo.objects.filter(id__gt=3))
    # year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
    # 查询1980年发表的图书
    print(BookInfo.objects.filter(bpub_date__year=1980))
    # 查询1980年1月1日后发表的图书
    print(BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1)))
    from django.db.models import F, Q
    print(BookInfo.objects.filter(bread__gte=F('bcomment')))
    # 查询阅读量大于2倍评论量的图书
    BookInfo.objects.filter(bread__gt=F('bcomment') * 2)
    # Q对象，多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字
    # 查询阅读量大于20，并且编号小于3的图书
    print(BookInfo.objects.filter(bread__gt=20, id__lt=3))
    # 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
    print(BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3)))
    # Q对象前可以使用~操作符，表示非not,如查询编号不等于3的图书
    print(BookInfo.objects.filter(~Q(pk=3)))
    return HttpResponse('query option')


class BooksView(View):
    def get(self, request):
        '''
        :param request:
        :return: 查询所有图书
        '''
        books = BookInfo.objects.all()
        # books_list = []
        # for book in books:
        #     books_list.append(book.btitle)
        #     books_list.append(book.bpub_date)
        # return JsonResponse({
        #     'books': books_list
        # })
        ser = BookSerializer(books, many=True)
        data = ser.data
        return JsonResponse(data, safe=False)

    def post(self, request):
        """
        :param request:
        :return: 新增图书
        """
        data = json.loads(request.body.decode())
        # ser = BookSerializer()
        # btitle = data.get('btitle')
        # bpub_date = data.get('bpub_date')
        # if btitle == 'python':
        #     return JsonResponse({'errors': '书名错误'}, status=400)
        # book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        #
        # return JsonResponse(
        #     {'id': book.id, 'btitle': book.btitle, 'bpub_date': book.bpub_date}
        # )


class BookView(View):

    def get(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 查询单一图书
        '''
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return JsonResponse({'errors': '未找到该书'})
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

    def put(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 修改图书
        '''
        data = json.loads(request.body.decode())
        btitle = data.get('btitle')
        bpub_date = data.get('bpub_date')
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return JsonResponse({'errors': '未找到该书'})
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return JsonResponse(
            {'id': book.id, 'btitle': book.btitle, 'bpub_date': book.bpub_date}
        )

    def delete(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 删除图书
        '''
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return JsonResponse({'errors': '未找到该书'})
        book.delete()
        return HttpResponse(status=204, content='删除成功！')
