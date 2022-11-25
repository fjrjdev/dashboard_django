from django.core.files.storage import default_storage

FILENAME = "CNAB.txt"


def write_file(file_obj):
    try:
        with default_storage.open("tmp/" + FILENAME, "wb+") as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        return True
    except:
        return False
