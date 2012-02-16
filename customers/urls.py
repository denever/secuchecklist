from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from customers.models import CustomerCompany, Staff

from customers.views import CustomerCompanyYearView
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

urlpatterns = patterns('customers.views',
		       url(r'^$', login_required(CustomerCompanyListView.as_view()),
			   name='customers'),

		       url(r'^(?P<pk>\d+)/$',
			   login_required(CustomerCompanyDetailView.as_view()),
			   name = 'company-detail'),

		       # url(r'^staff/(?P<pk>\d+)/$',
		       #     login_required(StaffDetailView.as_view()),
		       #     name = 'staff-detail'
		       #     ),

		       url(r'^(?P<company>\d+)/staff/(?P<pk>\d+)/$',
			   login_required(StaffDetailView.as_view()),
			   name = 'staff-detail'
			   ),

		       url(r'year/(?P<year>\d{4})/$',
			   login_required(CustomerCompanyYearView.as_view()),
			   name = 'company-year'
			   ),

		       url(r'^create/$',
			   login_required(CustomerCompanyCreateView.as_view()),
			   name = 'company-create'
			   ),

		       url(r'^(?P<company>\d+)/add_staff/$',
			   login_required(StaffCreateView.as_view()),
			   name = 'add-staff'
			   ),

		       url(r'^update/(?P<pk>\d+)/$',
			   login_required(CustomerCompanyUpdateView.as_view()),
			   name = 'edit-company'
			   ),

		       url(r'^update_staff/(?P<pk>\d+)/$',
			   login_required(StaffUpdateView.as_view()),
			   name = 'edit-staff'
			   ),

		       url(r'^delete/(?P<pk>\d+)/$',
			   login_required(CustomerCompanyDeleteView.as_view()),
			   name = 'delete-company'
			   ),

		       url(r'^delete_staff/(?P<pk>\d+)/$',
			   login_required(StaffDeleteView.as_view()),
			   name = 'delete-staff'
			   ),

		       url(r'^(?P<pk>\d+)/working_env/$',
			   login_required(WorkingEnvironmentEditView.as_view()),
			   name = 'set-working-env'
			   ),

		       url(r'^(?P<company>\d+)/add_department/$',
			   login_required(DepartmentCreateView.as_view()),
			   name = 'add-department'
			   ),

		       url(r'^department/(?P<pk>\d+)/$',
			   login_required(DepartmentDetailView.as_view()),
			   name = 'department-detail'
			   ),

		       url(r'^(?P<company>\d+)/staff/$',
			   login_required(StaffListView.as_view()),
			   name = 'staff-list'
			   ),
		       )
