from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings
from supabase import create_client
import mimetypes

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.bucket = settings.SUPABASE_BUCKET
        storage_obj = self.supabase.storage() if callable(self.supabase.storage) else self.supabase.storage
        if hasattr(storage_obj, 'from_'):
            self.bucket_client = storage_obj.from_(self.bucket)
        else:
            self.bucket_client = storage_obj.bucket(self.bucket)

    def _save(self, name, content):
        content.open()
        file_data = content.read()
        content.close()
        content_type, _ = mimetypes.guess_type(name)
        if not content_type:
            content_type = "application/octet-stream"
        self.bucket_client.upload(
            path=name,
            file=file_data,
            file_options={"contentType": content_type, "upsert": "true"}
        )
        return name

    def _open(self, name, mode='rb'):
        res = self.bucket_client.download(name)
        return ContentFile(res)

    def delete(self, name):
        self.bucket_client.remove([name])

    def exists(self, name):
        files = self.bucket_client.list()
        return any(f['name'] == name for f in files)

    def url(self, name):
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{self.bucket}/{name}"

    def size(self, name):
        files = self.bucket_client.list()
        for f in files:
            if f['name'] == name:
                return f.get('metadata', {}).get('size', 0)
        return 0