from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {
    "keywords": "Exterieur Chapelle Saint Joseph toulouse",
    "limit": 40,
    "output_directory": "dataset",
    "no_directory": True,
    "safe_search": True,
    "format": "jpg",
}

paths = response.download(arguments)
