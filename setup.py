from setuptools import setup, find_packages
import versioneer


setup(name='menpodetectthin',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Object detection for Menpo',
      author='Fergus Cooney (Adapted from Menpo Development Team)',
      author_email='fergus.cooney@ucd.ie',
      packages=find_packages(),
      tests_require=['nose'],
      install_requires=['menpo>=0.7,<0.8'])

