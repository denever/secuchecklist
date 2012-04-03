from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from customers.models import CustomerCompany, Staff

from customers.views import CustomerCompanyYearView
from customers.views import CustomerCompanyMonthView
from customers.views import CustomerCompanyListView
from customers.views import CustomerCompanyDetailView
from customers.views import CustomerCompanyCreateView
from customers.views import CustomerCompanyUpdateView
from customers.views import CustomerCompanyDeleteView

from customers.views import StaffListView
from customers.views import StaffDetailView
from customers.views import StaffCreateView
from customers.views import StaffUpdateView
from customers.views import StaffDeleteView

from customers.views import WorkingEnvironmentEditView

from customers.views import DepartmentCreateView
from customers.views import DepartmentDetailView
from customers.views import DepartmentUpdateView
from customers.views import DepartmentDeleteView

from customers.views import CompanySecurityDutyCreateView
from customers.views import CompanySecurityDutyListView
from customers.views import CompanySecurityDutyDetailView
from customers.views import CompanySecurityDutyUpdateView
from customers.views import CompanySecurityDutyDeleteView

from customers.views import MachineCreateView
from customers.views import MachineListView
from customers.views import MachineDetailView
from customers.views import MachineUpdateView
from customers.views import MachineDeleteView

urlpatterns = patterns('customers.views',
                       url(r'^$', login_required(CustomerCompanyListView.as_view()),
                           name='customers'),

                       url(r'^(?P<pk>\d+)/$',
                           login_required(CustomerCompanyDetailView.as_view()),
                           name = 'company-detail'),

                       url(r'^(?P<company>\d+)/staff/(?P<pk>\d+)/$',
                           login_required(StaffDetailView.as_view()),
                           name = 'staff-detail'
                           ),

                       url(r'year/(?P<year>\d{4})/$',
                           login_required(CustomerCompanyYearView.as_view()),
                           name = 'company-year'
                           ),

                       url(r'month/(?P<year>\d{4})/(?P<month>[A-Za-z]{3})/$',
                           login_required(CustomerCompanyMonthView.as_view()),
                           name = 'company-month'
                           ),

                       url(r'^create/$',
                           login_required(CustomerCompanyCreateView.as_view()),
                           name = 'company-create'
                           ),

                       url(r'^(?P<company>\d+)/add_staff/$',
                           login_required(StaffCreateView.as_view()),
                           name = 'staff-add'
                           ),

                       url(r'^(?P<pk>\d+)/update/$',
                           login_required(CustomerCompanyUpdateView.as_view()),
                           name = 'company-edit'
                           ),

                       url(r'^delete_company/(?P<pk>\d+)/$',
                           login_required(CustomerCompanyDeleteView.as_view()),
                           name = 'company-delete'
                           ),

                       url(r'^(?P<company>\d+)/update_staff/(?P<pk>\d+)/$',
                           login_required(StaffUpdateView.as_view()),
                           name = 'staff-edit'
                           ),

                       url(r'^(?P<company>\d+)/delete_staff/(?P<pk>\d+)/$',
                           login_required(StaffDeleteView.as_view()),
                           name = 'staff-delete'
                           ),

                       url(r'^(?P<pk>\d+)/working_env/$',
                           login_required(WorkingEnvironmentEditView.as_view()),
                           name = 'set-working-env'
                           ),

                       url(r'^(?P<company>\d+)/add_department/$',
                           login_required(DepartmentCreateView.as_view()),
                           name = 'department-add'
                           ),

                       url(r'^(?P<company>\d+)/update_department/(?P<pk>\d+)/$',
                           login_required(DepartmentUpdateView.as_view()),
                           name = 'department-edit'
                           ),

                       url(r'^(?P<company>\d+)/delete_department/(?P<pk>\d+)/$',
                           login_required(DepartmentDeleteView.as_view()),
                           name = 'department-delete'
                           ),

                       url(r'^(?P<company>\d+)/department/(?P<pk>\d+)/$',
                           login_required(DepartmentDetailView.as_view()),
                           name = 'department-detail'
                           ),

                       url(r'^(?P<company>\d+)/staff/$',
                           login_required(StaffListView.as_view()),
                           name = 'staff-list'
                           ),

                       url(r'^(?P<company>\d+)/add_secduty/$',
                           login_required(CompanySecurityDutyCreateView.as_view()),
                           name = 'companysecurityduty-add'
                           ),

                       url(r'^(?P<company>\d+)/secduty/(?P<pk>\d+)/$',
                           login_required(CompanySecurityDutyDetailView.as_view()),
                           name = 'companysecurityduty-detail'
                           ),

                       url(r'^(?P<company>\d+)/secduties/$',
                           login_required(CompanySecurityDutyListView.as_view()),
                           name = 'companysecurityduty-list'
                           ),

                       url(r'^(?P<company>\d+)/update_secduties/(?P<pk>\d+)/$',
                           login_required(CompanySecurityDutyUpdateView.as_view()),
                           name = 'companysecurityduty-edit'
                           ),

                       url(r'^(?P<company>\d+)/delete_secduties/(?P<pk>\d+)/$',
                           login_required(CompanySecurityDutyDeleteView.as_view()),
                           name = 'companysecurityduty-delete'
                           ),

                       url(r'^(?P<company>\d+)/add_machine/$',
                           login_required(MachineCreateView.as_view()),
                           name = 'machine-add'
                           ),

                       url(r'^(?P<company>\d+)/machine/(?P<pk>\d+)/$',
                           login_required(MachineDetailView.as_view()),
                           name = 'machine-detail'
                           ),

                       url(r'^(?P<company>\d+)/machines/$',
                           login_required(MachineListView.as_view()),
                           name = 'machine-list'
                           ),

                       url(r'^(?P<company>\d+)/update_machine/(?P<pk>\d+)/$',
                           login_required(MachineUpdateView.as_view()),
                           name = 'machine-edit'
                           ),

                       url(r'^(?P<company>\d+)/delete_machine/(?P<pk>\d+)/$',
                           login_required(MachineDeleteView.as_view()),
                           name = 'machine-delete'
                           ),

                       )
