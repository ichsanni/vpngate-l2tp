from setuptools import setup


setup(name='vpngate-l2tp',
  version='0.1',
  description='Create and connect to L2TP connection and use VPNGate servers.',
  url='https://github.com/ichsanni/vpngate-l2tp',
  author='Ichsan Nuur',
  author_email='ichsan@csar.co.jp',
  license='MIT',
  packages=['vpngate_l2tp'],
  zip_safe=False,
  install_requires=[
    "requests >= 2.26.0"])
