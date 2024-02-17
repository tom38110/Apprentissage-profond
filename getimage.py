from bing_image_downloader import downloader
downloader.download("Cathedrale Saint-Etienne toulouse", limit=200,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)