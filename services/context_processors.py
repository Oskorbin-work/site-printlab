from core.models import Contact


def up(request):
    return {'object_list': Contact.objects.filter(id=1)}