import time, datetime
from django.apps import apps
from django.db.models.query import QuerySet

from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from .datatables_helper import DatatableMixin #datatables_helper
from .models import serializer_factory
from communications.models import Messages
from admissions.models import Admission
from dashboard.models import SystemSettings

def CreateTokenResponse(serializer):
    # this can be used in mobileapi/views/UserLogin.py
    
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    # User check : status  and deleted_at
    if user.deleted_at is not None:
        return {'status':'1','message':'Your account has been deleted. Please contact administrator..!'}
    if user.status != 1:
        return {'status':'0','message':'User is not active. Please contact administrator..!'}

    token, created = Token.objects.get_or_create(user=user)
    sub_domain = SystemSettings.objects.filter(key = 'sub_domain')
    
    return {
        'token': token.key,
        'user_id': user.pk,
        'email': user.email,
        'username': user.username,
        'user_type' : user.user_type,
        'fullname': '%s %s'%(user.first_name, user.last_name),
        'sub_domain': sub_domain[0].value if sub_domain else ''
    }

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        resp = CreateTokenResponse(serializer)
        if 'status' in resp:
            return Response(resp,status=status.HTTP_400_BAD_REQUEST)
        return Response(resp)

class TimeDelayMixin(object, ):
    def dispatch(self, request, *args, **kwargs):
        time.sleep(1)
        return super().dispatch(request, *args, **kwargs)

class CURDViewSet(TimeDelayMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    # https://stackoverflow.com/a/26916875/2351696
    @classmethod
    def create_custom(self, **kwargs):
        class CustomViewSet(self):
            model = kwargs["model"]
            queryset = kwargs["model"].objects.filter(deleted_at=None, status =1)
            serializer_class = serializer_factory(kwargs["model"])
        return CustomViewSet

    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(created_by=req.user)

    def perform_update(self, serializer):
        req = serializer.context['request']
        serializer.save(updated_by=req.user)

    # def get_queryset(self):
    #     queryset = self.queryset
    #     if isinstance(queryset, QuerySet):
    #         # Ensure queryset is re-evaluated on each request.
    #         queryset = queryset.filter(deleted_at__isnull=True)
            
    #     return queryset

class TimeDelayed_APIView(TimeDelayMixin, APIView):
    pass

class DatatableListJson(DatatableMixin,TimeDelayed_APIView):
    """
    To fill Jquery Datatable
    In datatable.service.ts: 
    * getDatas: will make post request with 
        params such as model, filter. While page loads
    * toolbarAction: will make get request by Toolbar buttons
        to perform enable,disable,forcedelete etc

    """ 
    renderer_classes = (JSONRenderer, )

    def set_model(self,model_name):
        # Get Model from a string, eg: dashboard__Roles
        app,model = model_name.split('__')
        self.model = apps.get_model(app,model)

    def get(self,request):
        cid = request.GET.getlist('cid[]')
        action = request.GET.get('action')
        model_name = request.GET.get('model_name')

        """
        Needs to fill Teacher datatable,actually a model of Employee.
        """
        if (model_name == 'hr__Teacher'):
            #print('teacher')
            #queryset = self.model.objects.filter(emp_staff_type = 'Teacher')
            model_name = 'hr__Employeemaster'

        #     queryset = self.model.objects.filter(id__in=cid, admission_school__in=True)
        self.set_model(model_name)
        # if (request.GET.get('model_name') == 'students__studentmaster'):
        #     queryset = self.model.objects.filter(id__in=cid, admission_school__in=True)
        # else:
        queryset = self.model.objects.filter(id__in=cid)
        
        if action in ["enable", "disable"]:
            queryset.update(status = 1 if action =='enable' else 0)

        elif action in ["remove", "restore"]:
            queryset.update(deleted_at = None if action =='restore' else datetime.datetime.now())
            
        elif action == "forcedelete":
            queryset.delete()

        return Response('success')

    def post(self, request, format=None):
        model_name = request.data['model_name']
        if (model_name == 'hr__Teacher'):
            """
            Needs to fill Teacher datatable,actually a model of Employee.
            """
            model_name = 'hr__Employeemaster'

        self.set_model(model_name)
        # if (request.data['model_name'] == 'students__studentmaster'):
        #     print("true")
        self.columns = self.model.columns
        self.order_columns = self.model.order_columns
        context_data = self.get_context_data()
        context_data['fields'] = self.columns
        return Response(context_data)
    

    def render_column(self, row, column):
        if column == 'id':
            return '''
            <center><label class="icheck_checkboxcontainer checkbox-inline">
                <input type="checkbox" class="sub_checkbox" value="%d" name="cid[]" >
                <span class="checkmark"></span>
            </label></center>''' % row.id
        
        elif column == 'status':
            return '<i class="fa fa-check"></i> Active' if row.status == 1 else '<i class="fa fa-times"></i> Inactive'

        else:
            model_column = self.model.filter_objects.render_column(row=row, column=column, request=self.request)
            
            if model_column:
                return model_column
            return super().render_column(row, column) 
            

   
    def filter_queryset(self, qs): 
        filter_trashed = self.request.data.get('filter_trashed', None)
        if (self.request.data['model_name'] == 'students__studentmaster'):
            qs = qs.filter(admission_school=True)
        
        if (self.request.data['model_name'] == 'hr__Teacher'):
            qs = qs.filter(emp_details__emp_staff_type = 'T')
        if (filter_trashed == '1'):
            qs = qs.filter(deleted_at__isnull=False)
        else:
            qs = qs.filter(deleted_at__isnull=True)        

        filter_status = self.request.data.get('filter_status', None)        
        if (filter_status):
            if getattr(self.model, 'status', False):
                qs = qs.filter(status=int(filter_status))

        # columns = self.get_columns()
        params = {'request': self.request, 'search': self._querydict['search']['value']}
        qs = self.model.filter_objects.filter_queryset(qs=qs, params=params)
        return qs # super().filter_queryset(qs)
    
