from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator
from blog.models import Article

def hello_world(request):
    return HttpResponse("hello,world")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brirf_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_data
    return_str = 'title: %s, brief_content: %s,'\
                 'content: %s, articlr_id: %s, publish_date: %s' %(title,
                                                                   brirf_content,
                                                                   content,
                                                                   article_id,
                                                                   publish_date)
    return HttpResponse(return_str)
def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page',page)

    # list
    all_article = Article.objects.all()
    # 右边栏文章倒叙排序，取前三篇文章显示
    top3_article_list = Article.objects.order_by('-publish_data')[0:3]
    # one page one article
    paginator = Paginator(all_article, 1)
    page_num = paginator.num_pages
    print('page num:', page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    # xuanran data&&html
    return render(request, 'blog/index.html',
                  {
                      'article_list': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_page': previous_page,
                      'top3_article_list': top3_article_list
                  }
                  )
# 将想要的数据返回，多做了页面渲染而已
# 传入article_id，路径传参数
def get_detial_page(request,article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate (all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    # list
    # 指定第一个文章
    # curr_article = Article.objects.all()[0]
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article

                  }
                  )