from rest_framework.response import Response
from rest_framework.views import APIView
from utils.models import Feedback

class ChangeFeedback(APIView):
    def get(self,request): 

        Feedback.objects.filter(
            id = request.GET['id']).update(status=request.GET['status'])
        return Response()
class FeedbackResolvedStatus(APIView):
    def get(self,request): 

        Feedback.objects.filter(
            id = request.query_params['id']).update(status=2)
        return Response()
class FeedbackClosedStatus(APIView):
    def get(self,request): 

        Feedback.objects.filter(
            id = request.query_params['id']).update(status=4)
        return Response()

class getUserFeedback(APIView):
    """
    To get Show Fee Transactions of an autheniticated student
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
       
       userid  = request.user.id
       return Response()
