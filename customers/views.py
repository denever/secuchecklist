# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from customers.models import *

def list(request):
    ccs = CustomerCompany.objects.all().order_by('-record_date')
    tmpl = loader.get_template('customers/customers_list.html')
    cnt = Context({'cc_list': ccs})
    return HttpResponse(tmpl.render(cnt))

def customer_detail(request, customer_id):
    cc = CustomerCompany.objects.get(id=customer_id)
    staff = cc.staff_set.all()
    tmpl = loader.get_template('customers/customer_detail.html')
    cnt = Context({
            'staff_list': staff,
            'company': cc
            })
    return HttpResponse(tmpl.render(cnt))

def staff_detail(request, staff_id):
    s = Staff.objects.get(id=staff_id)
    output = "%s %s (%s)" % (s.surname, s.name, s.standard_task)
    return HttpResponse(output)
