from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

# def home(request):
#     # cache.get(key, name, expired time, version)
#     mv = cache.get('movie', 'has_expired')
#     if mv=='has_expired':
#         cache.set('movie', 'Iron Man', 30)
#         mv=cache.get('movie')
#     return render(request, 'course.html', {'caches':mv})

# def home(request):
#     # cache.get_or_set(key, name, expired time, version)
#     mv = cache.get_or_set('name', 'Haq', 30, version=2)
#     return render(request, 'course.html', {'caches':mv})

# def home(request):
#     # cache.get_or_set(key, name, expired time, version)
#     data = {'name':'Sonam', 'roll':34}
#     cache.set_many(data=data)
#     many = cache.get_many(data)
    # return render(request, 'course.html', {'caches':many})


# def home(request):
# #     # cache.get_or_set(key, name, expired time, version)
#     cache.delete('roll')
#     return render(request, 'course.html')

# def home(request):
#     # cache.get_or_set(key, name, expired time, version)
#     # cache.set('roll', 34, 30)
#     # mv = cache.get('roll')
#     # mv = cache.decr('roll', delta=1)
#     mv = cache.incr('roll', delta=1)
#     return render(request, 'course.html', {'cache':mv})

def home(request):
    # cache.get_or_set(key, name, expired time, version)
    cache.clear()
    return render(request, 'course.html')
