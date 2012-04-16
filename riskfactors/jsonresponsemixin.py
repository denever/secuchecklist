from django import http
from django.utils import simplejson as json
from django.core.urlresolvers import reverse

class RiskFactorNodeMixin(object):
    def render_to_response(self, context):
	"Returns a JSON response containing 'context' as payload"
	return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
	"Construct an `HttpResponse` object."
	return http.HttpResponse(content,
				 content_type='application/json',
				 **httpresponse_kwargs)

    def serialize_riskfactor(self, riskfactor):
	children = list()
	for child in riskfactor.children.all():
	    children.append(self.serialize_riskfactor(child))
	return dict(title=riskfactor.description,
		    children=children,
		    data=dict(id=riskfactor.id,
			      detail_url = reverse('riskfactor-detail', args=[riskfactor.id]),
			      edit_url = reverse('riskfactor-edit', args=[riskfactor.id]),
			      delete_url = reverse('riskfactor-delete', args=[riskfactor.id]),
			      add_url = reverse('riskfactor-add', args=[riskfactor.id])
			      )
		    )

    def convert_context_to_json(self, context):
	"Convert the context dictionary into a JSON object"
	# Note: This is *EXTREMELY* naive; in reality, you'll need
	# to do much more complex handling to ensure that arbitrary
	# objects -- such as Django model instances or querysets
	# -- can be serialized as JSON.
	return json.dumps(self.serialize_riskfactor(context['riskfactor']))

class RiskFactorSubTreeMixin(object):
    def render_to_response(self, context):
	"Returns a JSON response containing 'context' as payload"
	return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
	"Construct an `HttpResponse` object."
	return http.HttpResponse(content,
				 content_type='application/json',
				 **httpresponse_kwargs)

    def serialize_riskfactor(self, riskfactor):
	return dict(title=riskfactor.description,
		    children=[],
		    data=dict(id=riskfactor.id,
			      detail_url = reverse('riskfactor-detail', args=[riskfactor.id]),
			      edit_url = reverse('riskfactor-edit', args=[riskfactor.id]),
			      delete_url = reverse('riskfactor-delete', args=[riskfactor.id]),
			      add_url = reverse('riskfactor-add', args=[riskfactor.id])
			      )
		    )

    def convert_context_to_json(self, context):
	"Convert the context dictionary into a JSON object"
	# Note: This is *EXTREMELY* naive; in reality, you'll need
	# to do much more complex handling to ensure that arbitrary
	# objects -- such as Django model instances or querysets
	# -- can be serialized as JSON.
	children = list()
	riskfactor = context['riskfactor']
	for child in riskfactor.children.all():
	    children.append(self.serialize_riskfactor(child))
	return json.dumps(children)
