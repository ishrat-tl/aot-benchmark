from setuptools import setup

setup(
    name='DeAOT',
    version='0.1.0',
    description='A semi-supervised video object segmentation approach.',
    url='https://github.com/ishrat-tl/aot-benchmark',
    author='Yang Zongxin',
    license='BSD-3 clause',
    packages=['configs',
              'configs/models',
              'dataloaders',
              'networks',
              'utils'],

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD-3 clause',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    info='This is an official implementation for DeAOT: Decoupling Features in Hierarchical Propagation for Video Object Segmentation (NeurIPS 2022)'
)
