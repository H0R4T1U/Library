from django.shortcuts import render,redirect
from .models import Carte
from django.db.models import Q

def index(request):
    try:
        searchString = request.GET["searchString"]
        searchParam = request.META["QUERY_STRING"]
        searchParam = searchParam.split("&searchParam=")[1::]

        books = _filter_query(searchParam,searchString)
        """
            OR (|)¶

            Combines two QuerySets using the SQL OR operator.

            The following are equivalent:

            Model.objects.filter(x=1) | Model.objects.filter(y=2)
            from django.db.models import Q
            Model.objects.filter(Q(x=1) | Q(y=2))


        """
        context = { 'books':books }
    except:

        books = Carte.objects.all()
        context = { 'books':books }
    return render(request,'main/index.html',context)


#not proud of this implementation
def _filter_query(params,searchString):
    books = Carte.objects.all()
    
    #implementeaza cu switch dupa 3.10 update!!!
    if len(params) == 4:
        books = books.filter(Q(name__contains= searchString) | Q(author__contains = searchString)| Q(location__contains = searchString)|Q(extra__contains = searchString) )
    elif len(params) == 3:
        if 'name' in params[0]:
            if 'author' in params[1]:
                if 'location' in params[2]:
                    books = books.filter(Q(name__contains= searchString) | Q(author__contains = searchString)| Q(location__contains = searchString))
                else:
                    books = books.filter(Q(name__contains= searchString) | Q(author__contains = searchString)|Q(extra__contains = searchString))
            else:
                books = books.filter(Q(name__contains= searchString) | Q(location__contains = searchString)|Q(extra__contains = searchString) )
        else:
            books =  books.filter(Q(author__contains = searchString) | Q(location__contains = searchString)|Q(extra__contains = searchString))
    
    elif len(params) == 2:
        if 'name' in params[0]:
            if 'author' in params[1]:
                books = books.filter(Q(name__contains= searchString) | Q(author__contains = searchString))
            elif 'location' in params[1]:
                books = books.filter(Q(name__contains= searchString) | Q(location__contains = searchString))
            else :
                books = books.filter(Q(name__contains= searchString) | Q(extra__contains = searchString) )

        elif 'author' in params[0]:
            if 'location' in params[1]:
                books = books.filter(Q(author__contains= searchString) | Q(location__contains = searchString))
            else :
                books = books.filter(Q(author__contains= searchString) | Q(extra__contains = searchString) )

        else:
            books = books.filter(Q(location__contains = searchString) | Q(extra__contains = searchString))

    elif len(params) == 1:
        if 'name' in params[0]:
            books = books.filter(name__contains =searchString)
        elif 'author' in params[0]:
            books = books.filter(author__contains = searchString)
        elif 'location' in params[0]:
            books = books.filter(location__contains = searchString)
        elif 'extra' in params[0]:
            books = books.filter(extra__contains = searchString)
    
    return books
