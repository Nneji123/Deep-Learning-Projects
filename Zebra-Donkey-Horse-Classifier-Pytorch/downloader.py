from bing_image_downloader import downloader
downloader.download('donkeys', limit=2000,  output_dir='', page_limit=3000, adult_filter_off=True, force_replace=False, timeout=20, resize=(224,224) ,verbose=True)

