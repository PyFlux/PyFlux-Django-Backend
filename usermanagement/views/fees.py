from fees.models import FeePaymentTransaction
from fees.serializers import FeePaymentTransactionSerializer

from shared.views import TimeDelayed_APIView
from rest_framework.response import Response

class getFeeTransactions(TimeDelayed_APIView):
    """
    To get Show Fee Transactions of an autheniticated student
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        if hasattr(request.user, 'student'):
            transactions = FeePaymentTransaction.objects.filter(student = request.user.student,)
            serializer = FeePaymentTransactionSerializer(transactions, many= True)
            return Response(serializer.data)
        return Response([])
