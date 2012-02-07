# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from customers.models import *

def list(request):
    ccs = CustomerCompany.objects.all().order_by('-record_date')
    # tmpl = loader.get_template('customers/customers_list.html')
    # cnt = Context({'cc_list': ccs})
    # return HttpResponse(tmpl.render(cnt))
    return render_to_response('customers/customers_list.html', {'cc_list': ccs})

def customer_detail(request, customer_id):
    # cc = CustomerCompany.objects.get(id=customer_id)
    # staff = cc.staff_set.all()
    # tmpl = loader.get_template('customers/customer_detail.html')
    # cnt = Context({
    #         'staff_list': staff,
    #         'company': cc
    #         })
    # return HttpResponse(tmpl.render(cnt))
    cc = get_object_or_404(CustomerCompany, pk=customer_id)
    staff = cc.staff_set.all()
    return render_to_response('customers/customer_detail.html',
                              {'staff_list': staff, 'company': cc})
def staff_detail(request, staff_id):
#    s = Staff.objects.get(id=staff_id)
    s = get_object_or_404(Staff, pk=staff_id)
    return render_to_response('customers/staff_detail.html',
                              {'staff': s})
