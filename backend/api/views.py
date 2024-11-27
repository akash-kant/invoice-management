from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice

class InvoiceAPIView(APIView):
    def get(self, request):
        invoices = Invoice.objects.all().values()
        return Response(invoices, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data
            invoice = Invoice.objects.create(
                client_name=data.get('client_name'),
                client_email=data.get('client_email'),
                invoice_number=data.get('invoice_number'),
                amount=data.get('amount'),
                due_date=data.get('due_date'),
            )
            return Response({"message": "Invoice created successfully!", "id": invoice.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": "Failed to create invoice.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
