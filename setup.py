from setuptools import setup, find_packages

setup(
    name='spotify_uri',
    version='1.0.0',
    description='This is a project that ported @TooTallNate/spotify-uri to Python.',
    author='zeroday0619',
    author_email='zeroday0619@kakao.com',
    url='https://github.com/zeroday0619/pyspotify-uri',
    packages=find_packages(exclude=['.vscode', '.idea']),
    keywords=[
        "spotify", "spotify-uri"
    ],
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)