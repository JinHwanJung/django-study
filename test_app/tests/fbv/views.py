from tests.fbv.models import Item
from django.shortcuts import render


def items(request):
    qs = Item.objects.all()
    return render(request, 'fbv/items.html', {'items': qs})
