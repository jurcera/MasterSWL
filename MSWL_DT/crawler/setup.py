from setuptools import setup, find_packages

setup( name = "SusoCrawler",
       version = "0.1",
       packages = find_packages(),
       scripts = ['susocrawler'],
       install_requires = ['BeautifulSoup'],
       package_data = { 'pysusocrawler': [''], },
       author = "Jesus Urcera",
       author_email = "jurcera@gmail.com",
       description = "Araña en internet",
       license = "",
       keywords = "",
       url = "",
       long_description = "",
       download_url = "" )
