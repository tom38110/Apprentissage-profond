from bing_image_downloader import downloader
downloader.download("hôtel d'Assezat toulouse", limit=200,  output_dir='Hotel_Assezat', 
                    adult_filter_off=True, force_replace=False, timeout=60)