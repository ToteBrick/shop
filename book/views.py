from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from book.models import BookInfo, HeroInfo


# Create your views here.

# 增加操作
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
