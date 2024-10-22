from django.shortcuts import render
from .forms import SearchForm
from searchengine_front.utils.firebase import search_pages_by_content

def search_view(request):
    form = SearchForm()
    query = request.GET.get('query')
    results = []
    if query:
        results = search_pages_by_content(query)
    return render(request, 'search/search.html', {'form': form, 'results': results, 'query': query})
