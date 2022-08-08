from setuptools import setup,find_packages

setup(name="cogreload", 
      version="0.0.1",
      description="Automatic Cog reloader for discord.py",
      long_description=open("readme.md").read(),
      long_description_content_type="text/markdown",
      packages=find_packages(),
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Topic :: Utilities",
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      "Programming Language :: Python :: 3.8",
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      "Intended Audience :: Developers",
      "Natural Language :: English"
      ]
      )