from typing import List, Union


def get_file_size(file_size: int) -> List[Union[int, str]]:
    unit: str = "Bytes"

    if (file_size >= 1000) & (file_size < 1000000):
        file_size = round(file_size / 1000, 2)
        unit = "KB"
    elif (file_size >= 1000000) & (file_size <= 1000000000):
        file_size = round(file_size / 1000 / 1000, 2)
        unit = "MB"
    elif file_size > 1000000000:
        file_size = round(file_size / 1000 / 1000 / 1000, 2)
        unit = "GB"

    return [file_size, unit]


image = ["image/jpeg",
         "image/jpx",
         "image/png",
         "image/gif",
         "image/webp",
         "image/x-canon-cr2",
         "image/tiff",
         "image/bmp",
         "image/vnd.ms-photo",
         "image/vnd.adobe.photoshop",
         "image/x-icon",
         "image/heic"]

video = ["video/mp4",
         "video/x-m4v",
         "video/x-matroska",
         "video/webm",
         "video/quicktime",
         "video/x-msvideo",
         "video/x-ms-wmv",
         "video/mpeg",
         "video/x-flv"]

audio = ["audio/midi",
         "audio/mpeg",
         "audio/m4a",
         "audio/ogg",
         "audio/x-flac",
         "audio/x-wav",
         "audio/wav",
         "audio/amr"]

archive = ["application/epub+zip",
           "application/zip",
           "application/x-tar",
           "application/x-zip-compressed",
           "application/x-rar-compressed",
           "application/gzip",
           "application/x-bzip2",
           "application/x-7z-compressed",
           "application/x-xz",
           "application/x-msdownload",
           "application/x-shockwave-flash",
           "application/rtf",
           "application/octet-stream",
           "application/postscript",
           "application/x-sqlite3",
           "application/x-nintendo-nes-rom",
           "application/x-google-chrome-extension",
           "application/vnd.ms-cab-compressed",
           "application/x-deb",
           "application/x-unix-archive",
           "application/x-compress",
           "application/x-lzip"]

document = ["application/msword",
            "application/pdf",
            "application/vnd.ms-powerpoint",
            "application/vnd.ms-excel",
            "text/plain"
            ]
