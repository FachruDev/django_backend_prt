from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings
from supabase import create_client
import mimetypes

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.bucket = settings.SUPABASE_BUCKET

    def _save(self, name, content):
        # Baca konten file
        content.open()
        file_data = content.read()
        content.close()
        # Tentukan content-type
        content_type, _ = mimetypes.guess_type(name)
        if not content_type:
            content_type = "application/octet-stream"
        # Upload ke Supabase Storage
        self.supabase.storage.from_(self.bucket).upload(
            path=name,
            file=file_data,
            file_options={"content-type": content_type, "upsert": True}
        )
        return name

    def _open(self, name, mode='rb'):
        # Download file dari Supabase Storage
        res = self.supabase.storage.from_(self.bucket).download(name)
        return ContentFile(res)

    def delete(self, name):
        # Hapus file dari Supabase Storage
        self.supabase.storage.from_(self.bucket).remove([name])

    def exists(self, name):
        # Cek apakah file ada di Supabase Storage
        files = self.supabase.storage.from_(self.bucket).list()
        return any(f['name'] == name for f in files)

    def url(self, name):
        # Generate public URL
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{self.bucket}/{name}"

    def size(self, name):
        # Dapatkan ukuran file (dalam byte)
        files = self.supabase.storage.from_(self.bucket).list()
        for f in files:
            if f['name'] == name:
                return f.get('metadata', {}).get('size', 0)
        return 0