
from distutils.core import setup
setup(
  name = 'easyflask',        
  packages = ['easyflask'],   
  version = '0.1',      
  license='MIT',        
  description = 'An easier and more simple version of flask.',
  author = 'WhMonkey',                   
  author_email = 'no-reply@no-reply.com',      
  url = 'https://github.com/whineymonkey10/ezflask',   
  download_url = 'https://github.com/WhineyMonkey10/EzFlask/archive/refs/tags/v.0.1.0.tar.gz',    
  keywords = ['FLASK', 'WEBSITE', 'EASY'],   
  install_requires=[            
          'flask',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)