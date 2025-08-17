from django.db import models
from solo.models import SingletonModel

# Model for contact form
class ContactForm(models.Model):
    email = models.EmailField(verbose_name="Email Pengirim")
    subject = models.CharField(max_length=255, verbose_name="Subjek")
    message = models.TextField(verbose_name="Pesan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Diterima pada")

    def __str__(self):
        return f"Pesan dari {self.email} perihal '{self.subject}'"

    class Meta:
        verbose_name = "Pesan Kontak Masuk"
        verbose_name_plural = "Pesan Kontak Masuk"
        ordering = ['-created_at']

# Model for contact information
class ContactInformation(SingletonModel):
    email_address = models.EmailField(verbose_name="Alamat Email")
    phone = models.CharField(max_length=30, verbose_name="Nomor Telepon")
    location = models.CharField(max_length=255, verbose_name="Lokasi")

    def __str__(self):
        return "Informasi Kontak"

    class Meta:
        verbose_name = "Informasi Kontak"
        verbose_name_plural = "Informasi Kontak"