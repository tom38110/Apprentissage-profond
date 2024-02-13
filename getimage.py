from bing_image_downloader import downloader
downloader.download("capitole toulouse", limit=200,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)