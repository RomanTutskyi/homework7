from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.1',
      description='Very useful code',
      url='https://github.com/Laplas00/module7/blob/main/clear_folder/setup.py',
      author='Bogdan Gaidarzhy',
      author_email='romachikkj@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.sorting:main']})