import setuptools

setuptools.setup(
    name="crypto_data-afriedsam", # Replace with your own username
    version="0.0.1",
    author="Aidan Friedsam",
    author_email="adf@thefriedsams.com",
	description='Fetch cryptocurrency prices',
	url="https://github.com/afriedsam/crypto_data_python_module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)