from django.shortcuts import render
import pandas as pd
import os, glob
from .models import Shares
from EquityListings.settings import BASE_DIR
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def convertDataToCSV(mylist, fname):
    d = {}
    co = []; na = []; op = []; hi = []; lo = []; cl = []

    for l in mylist:

        co.append(l.code)
        na.append(l.name)
        op.append(l.open)
        hi.append(l.high)
        lo.append(l.low)
        cl.append(l.close)


    d['code'] = co
    d['name'] = na
    d['open'] = op
    d['high'] = hi
    d['low'] = lo
    d['close'] = cl

    df = pd.DataFrame(d)

    # saving the dataframe
    df.to_csv(os.path.join(BASE_DIR,"stocks","static","stocks",f"{fname}.csv"))


def index(request):

    context = {
        "data":None,
    }

    if request.method =='POST':
        f = request.POST.get("c_name")

        if cache.get(f):
            data = cache.get(f)
            print("getting data from cache")
        else:
            data = Shares.objects.filter(name__contains = f)
            cache.set(f, data)
            print("setting the data to cache")

            convertDataToCSV(data,f)

        context["data"] = data
        context['file'] = f"{f}.csv"
        print(context["file"])
    else:
        filelist = glob.glob(os.path.join(os.path.join(BASE_DIR,"stocks","static","stocks"), "*"))
        for f in filelist:
            os.remove(f)

    return render(request, "base.html", context=context)







