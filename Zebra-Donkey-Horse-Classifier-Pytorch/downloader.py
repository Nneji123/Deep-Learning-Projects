# from bing_image_downloader import downloader
# downloader.download('Zebra images', limit=2000,  output_dir='Zebra', page_limit=1000, adult_filter_off=True, force_replace=False, timeout=20, resize=(224,224) ,verbose=True)

# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

# search_queries =
# [
	
# 'The smartphone also features an in display fingerprint sensor.',
# 'The pop up selfie camera is placed aligning with the rear cameras.',
# '''In terms of storage Vivo V15 Pro could offer
# up to 6GB of RAM and 128GB of onboard storage.''',
# 'The smartphone could be fuelled by a 3 700mAh battery.',
# ]


def downloadimages(query):
	# keywords is the search query
	# format is the image file format
	# limit is the number of images to be downloaded
	# print urs is to print the image file url
	# size is the image size which can
	# be specified manually ("large, medium, icon")
	# aspect ratio denotes the height width ratio
	# of images to download. ("tall, square, wide, panoramic")
	arguments = {"keywords": query,
				"format": "jpg",
				"limit":2000,
				"print_urls":True,
				"size": "medium",
                "chromedriver": "chromedriver",
				"aspect_ratio":"panoramic"}
	try:
		response.download(arguments)
	
	# Handling File NotFound Error	
	except FileNotFoundError:
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":2000,
					"print_urls":True,
					"size": "medium",
                    "chromedriver": "chromedriver"}
					
		# Providing arguments for the searched query
		try:
			# Downloading the photos based
			# on the given arguments
			response.download(arguments)
		except:
			pass


downloadimages('Zebra images')
print()

python3 bing_scraper.py --url 'https://www.bing.com/images/search?q=zebras' --limit 2000 --download 