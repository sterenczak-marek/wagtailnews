from django.conf import settings
from django.utils.module_loading import import_string

try:
    name = settings.WAGTAILNEWS_PAGINATOR
except AttributeError:
    from django.core.paginator import Paginator, EmptyPage
    
    try:
        items_per_page = settings.WAGTAILNEWS_NEWS_PER_PAGE
    except AttributeError:
        items_per_page = 20

    def paginate(request, items):
        paginator = Paginator(items, items_per_page)

        try:
            page_number = int(request.GET['page'])
            page = paginator.page(page_number)
        except (ValueError, KeyError, EmptyPage):
            page = paginator.page(1)

        return paginator, page

else:
    paginate = import_string(name)
