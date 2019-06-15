import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import date

from django.views import View

from book.models import BookInfo, HeroInfo

# 增加操作
from book.serializers import BookSerializer, BookModelSerializer


class BooksView(View):
    def get(self, request):
        '''
        :param request:
        :return: 查询所有图书
        '''
        books = BookInfo.objects.all()
        ser = BookModelSerializer(books, many=True)
        return JsonResponse(ser.data, safe=False)
        # books_list = []
        # for book in books:
        #     books_list.append(book.btitle)
        #     books_list.append(book.bpub_date)
        # return JsonResponse({
        #     'books': books_list
        # })

    def post(self, request):
        """
        :param request:
        :return: 新增图书
        """
        data = json.loads(request.body.decode())
        ser = BookSerializer(data=data)
        ser.is_valid(raise_exception=True)
        print(ser.errors)
        ser.save()
        return JsonResponse(ser.data)


class BookView(View):
    def put(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 修改图书
        '''
        data = json.loads(request.body.decode())
        # btitle = data.get('btitle')
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return JsonResponse({'errors': '未找到该书'})

        ser = BookSerializer(book, data=data)
        ser.is_valid()
        ser.save()
        return JsonResponse(ser.data)

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
