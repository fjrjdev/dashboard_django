from django.core.files.storage import default_storage

filename = "CNAB.txt"


def write_file(file_obj):
    try:
        with default_storage.open("tmp/" + filename, "wb+") as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        return True
    except:
        return False
