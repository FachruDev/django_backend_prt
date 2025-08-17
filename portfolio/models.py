from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField

# Model for certificate
class Certificate(models.Model):
    title = models.CharField(max_length=255, verbose_name="Judul Sertifikat")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Subjudul")
    issuedby = models.CharField(max_length=150, verbose_name="Diterbitkan oleh")
    issuedon = models.DateField(blank=True, null=True, verbose_name="Tanggal Terbit")
    valid_until = models.DateField(blank=True, null=True, verbose_name="Berlaku Hingga")
    credential_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Kredensial")
    certificate_image = models.ImageField(upload_to='portfolio/certificates/images/', verbose_name="Gambar Sertifikat")
    pdf_certificate = models.FileField(upload_to='portfolio/certificates/pdfs/', blank=True, null=True, verbose_name="File PDF Sertifikat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikat"
        ordering = ['-issuedon']

# Model for project category
class ProjectCategory(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Judul Kategori")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategori Proyek"
        verbose_name_plural = "Kategori Proyek"

# Model for project
class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Judul Proyek")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Subjudul")
    description = RichTextField(verbose_name="Deskripsi")
    issued_on = models.DateField(blank=True, null=True, verbose_name="Tanggal Pengerjaan")
    role = models.CharField(max_length=100, verbose_name="Peran")
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects',
        verbose_name="Kategori"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proyek"
        verbose_name_plural = "Proyek"
        ordering = ['-issued_on']

# Model for project image
class ImageProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="Proyek Terkait")
    image = models.ImageField(upload_to='portfolio/projects/images/', verbose_name="Gambar")
    featured_image_url = models.URLField(max_length=1024, blank=True, verbose_name="URL Gambar Unggulan (jika eksternal)")
    featured_image_alt = models.CharField(max_length=255, blank=True, verbose_name="Teks Alternatif Gambar")

    def __str__(self):
        return f"Gambar untuk {self.project.title}"

    class Meta:
        verbose_name = "Gambar Proyek"
        verbose_name_plural = "Gambar Proyek"

# Model for experience
class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name="Posisi/Jabatan")
    role = models.CharField(max_length=150, verbose_name="Peran")
    company = models.CharField(max_length=150, verbose_name="Perusahaan")
    work_on = models.CharField(max_length=100, verbose_name="Waktu Bekerja", help_text="Contoh: Jan 2022 - Present")
    company_location = models.CharField(max_length=150, verbose_name="Lokasi Perusahaan")

    def __str__(self):
        return f"{self.title} di {self.company}"

    class Meta:
        verbose_name = "Pengalaman"
        verbose_name_plural = "Pengalaman"
        ordering = ['-id']

# Model for achievement experience
class AchievementExperience(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='achievements', verbose_name="Pengalaman Terkait")
    description = RichTextField(verbose_name="Deskripsi Pencapaian")

    def __str__(self):
        return f"Pencapaian untuk {self.experience.title}"

    class Meta:
        verbose_name = "Pencapaian Pengalaman"
        verbose_name_plural = "Pencapaian Pengalaman"

# Model for skills category
class SkillsCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="Judul Kategori")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Ikon", help_text="Contoh: 'fab fa-python' atau path SVG")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategori Skill"
        verbose_name_plural = "Kategori Skill"

# Model for skill
class Skill(models.Model):
    class Status(models.TextChoices):
        EXPERT = 'expert', 'Expert'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        BEGINNER = 'beginner', 'Beginner'

    title = models.CharField(max_length=100, verbose_name="Nama Skill")
    percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Persentase Keahlian"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.INTERMEDIATE,
        verbose_name="Level Keahlian"
    )
    icon = models.CharField(max_length=100, blank=True, verbose_name="Ikon", help_text="Contoh: 'fab fa-react' atau path SVG")
    
    category = models.ForeignKey(SkillsCategory, on_delete=models.CASCADE, related_name='skills', verbose_name="Kategori")
    
    projects = models.ManyToManyField(Project, blank=True, related_name='related_skills', verbose_name="Terkait Proyek")
    certificates = models.ManyToManyField(Certificate, blank=True, related_name='related_skills', verbose_name="Terkait Sertifikat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"