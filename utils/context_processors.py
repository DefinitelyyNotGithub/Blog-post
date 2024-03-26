from Blog_Post.models import Post, Category
from Main_page.models import site_general_info
from Blog_Post.models import Post


def recent_posts(request):
    value = Post.objects.order_by('-spread_date')[:5]
    return {'recent_post': value}

def cat(request):
    value = Category.objects.all()[:12]
    return {"cat": value}

def general_info(request):
    x = site_general_info.objects.last()
    return {'site_general_info': x}

def popular_tags(request):
    obj = Post.tags.most_common()[:8]
    return {'popular_tags': obj}

