import sys
sys.path.append("../")

from django.shortcuts import get_object_or_404

from .models import WildBlog, WebPageContentLocation
from maayan_wild_blog.views import display_page

# Create your views here.

def blog_page_display(request, blog_name, page_name):
    
    blog = get_object_or_404(WildBlog, pk = blog_name)
    page = get_object_or_404(WebPageContentLocation, pk = page_name)
    ans  = display_page(request, page.path, blog.path)
    return ans
    
