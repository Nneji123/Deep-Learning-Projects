from bing_image_downloader import downloader
downloader.download('Zebra images', limit=2000,  output_dir='Zebra', page_limit=1000, adult_filter_off=True, force_replace=False, timeout=20, resize=(224,224) ,verbose=True)

