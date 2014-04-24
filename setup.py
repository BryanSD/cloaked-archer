# -*- coding: utf-8 -*-
try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    import setuptools

setuptools.setup(
    name='cloaked_archer',
    version='0.1',
    description='',
    author='',
    author_email='',
    install_requires=[
        "bottle",
    ],
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_packages(exclude=['ez_setup']),
    entry_points={'cloaked_archer.db_drivers': [
        'memory = driver_memory:MemoryDriver',
        'cassandra = driver_cassandra:CassandraDriver',
        'postgresql = driver_postgresql:PostgreSQLDriver',
        'mongo = driver_mongo:MongoDriver']}
)
