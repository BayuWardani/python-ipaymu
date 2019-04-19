import setuptools


setuptools.setup(
     name='python-ipaymu',  
     version='0.1',
     scripts=['ipaymu'] ,
     author="Bayu Wardani",
     author_email="bayuwardani51@gmail.com",
     description="Integrasi iPaymu",
     long_description="Memudahkan ada bagi pengguna python untuk integrasi dengan iPaymu",
     long_description_content_type="text/markdown",
     url="https://github.com/BayuWardani/python-ipaymu.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "iPaymu",
     ],
 )