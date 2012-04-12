from django import http
from django.utils import simplejson as json
from django.core.urlresolvers import reverse

class RiskFactorJsonResponseMixin(object):
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
        return dict(label=riskfactor.description, children=children,
                    detail_url = reverse('riskfactor-detail', args=[riskfactor.id]),
                    edit_url = reverse('riskfactor-edit', args=[riskfactor.id]),
                    delete_url = reverse('riskfactor-delete', args=[riskfactor.id]),
                    )
    
    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        rfs = list()
        for rf in context['riskfactor_list']:
            rfs.append(self.serialize_riskfactor(rf))
        return json.dumps(rfs)
