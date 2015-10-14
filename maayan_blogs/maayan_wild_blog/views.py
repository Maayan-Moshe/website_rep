from django.shortcuts import render
import os

# Create your views here.

def display_page(request, page_content_location, father_path):
    
    context = get_context_for_page(father_path)
    template_path = os.path.join(father_path, page_content_location.path)
    return render(request, template_path, context)
    
def get_context_for_page(father_path):
    
    context = dict()
    header_path = os.path.join(father_path, 'headr.html')
    header_file = open(header_path)
    context['header_content'] = header_file.read()
    header_file.close()
    return context
