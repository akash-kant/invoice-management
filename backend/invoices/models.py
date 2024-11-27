from django.db import models

class Invoice(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    invoice_number = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.client_name}"


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="details", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for {self.invoice.invoice_number}: {self.description}"
