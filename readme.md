PiMC
=================

PiMC is a voice recognition server with varoius sunctionality and a client app to manage devices accounts and settings

Supported Speech recognition engines:

* CMU Sphinx `<http://cmusphinx.sourceforge.net/wiki/>`__ (works offline)
* Google Speech Recognition
* Google Cloud Speech API `<https://cloud.google.com/speech/>`
* Wit.ai `<https://wit.ai/>`
* Microsoft Bing Voice Recognition `<https://www.microsoft.com/cognitive-services/en-us/speech-api>`
* Houndify API `<https://houndify.com/>`
* IBM Speech to Text `<http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/speech-to-text.html>`

Requirements
------------

* **Python** 3.3+ (required) `https://www.python.org/`
* **PyAudio** 0.2.9+ (required for microphone input/audio playback) `http://people.csail.mit.edu/hubert/pyaudio/docs/`
* **Flask**`0.12+ (required for rest api) http://flask.pocoo.org/docs/0.12/deploying/cgi/#server-setup`
* **PYWAPI** (required for weather searching)`https://code.google.com/archive/p/python-weather-api/`
* **gTTS** (required for text to speech) `https://github.com/pndurette/gTTS`
* **Spotipy** (required for spotify music playback) `https://github.com/plamere/spotipy`
* **PocketSphinx** (required only if you need to use the Sphinx recognizer)
* **Google API Client Library for Python** (required only if you need to use the Google Cloud Speech API)
* **FLAC encoder** (required only if the system is not x86-based Windows/Linux/OS X) - no install required, included as binaries
* **Pygame** (required for playback of TTS files. Only imports the mixer module)

* If using CMU Sphinx, you may want to `install additional language packs <https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst#installing-other-languages>`

Installing
----------
Python
* download python from `https://www.python.org/`
* Add Python to your PATH envoirnment variable

PyAudio
* On Windows, install PyAudio using `Pip <https://pip.readthedocs.org/>`__: execute ``pip install pyaudio`` in a terminal.
* On Debian-derived Linux distributions, install PyAudio using `APT <https://wiki.debian.org/Apt>`__: execute ``sudo apt-get install python-pyaudio python3-pyaudio``
    * If the version in the repositories is too old, install the latest release using Pip: execute ``sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio`` (replace ``pip`` with ``pip3`` if using Python 3).
* On OS X, install PortAudio using `Homebrew <http://brew.sh/>`__: ``brew install portaudio && sudo brew link portaudio``. Then, install PyAudio using `Pip <https://pip.readthedocs.org/>`__: ``pip install pyaudio``.
* On other POSIX-based systems, install the ``portaudio19-dev`` and ``python-all-dev`` (or ``python3-all-dev`` if using Python 3) packages (or their closest equivalents) using a package manager of your choice, and then install PyAudio using `Pip <https://pip.readthedocs.org/>`__: ``pip install pyaudio`` (replace ``pip`` with ``pip3`` if using Python 3).

Flask
* On Windows, install Flask using `pip install flask`
* On Unix Based Systems install flask using `$ pip install flask`

PYWAPI
Download the latest pywapi library from: https://launchpad.net/python-weather-api/trunk/0.3.8/+download/pywapi-0.3.8.tar.gz
Untar the source distribution and run: $ python setup.py build $ python setup.py install
* On Windows, `python setup.py build`  `python setup.py install`
* On Unix Based Systems, `$ python setup.py build $ python setup.py install`

gTTs
* On Windows, install Flask using `pip install gTTS`
* On Unix Based Systems install flask using `$ pip install gTTS`

Spotipy
* On Windows, install Flask using `pip install spotipy`
* On Unix Based Systems install flask using `$ pip install spotipy`

Pygame
* On Windows, install pygame using `pip install pygame`

Py-Require
* On Windows, install Py-Require using `pip install py-require`

Environment
----------
Dowload and install Webstorm and pycharm, both are available for free if you use your mohowk accounts
Open Server folder in pycharm
Open Client folder in webstorm

Running
----------
To run the front end in dev mode, open the index file in webstorm and launch using the chrome icon in the top right corner

To run the server in dev mode, right click the "__main__" file in pycharm and run it

Testing
----------



Binaries
----------

The included ``flac-win32`` executable is the `official FLAC 1.3.1 32-bit Windows binary <http://downloads.xiph.org/releases/flac/flac-1.3.1-win.zip>`__.

The included ``flac-linux-x86`` and ``flac-linux-x86_64`` executables are built from the `FLAC 1.3.1 source code <http://downloads.xiph.org/releases/flac/flac-1.3.1.tar.xz>`__ with `Manylinux <https://github.com/pypa/manylinux>`__ to ensure that it's compatible with a wide variety of distributions.

The included ``flac-mac`` executable is extracted from `xACT 2.38 <http://xact.scottcbrown.org/>`__, which is a frontend for FLAC that conveniently includes binaries for all of its encoders. Specifically, it is a copy of ``xACT 2.38/xACT.app/Contents/Resources/flac`` in ``xACT2.38.zip``.

Library References
-----------------

* Speech Recognition wrapper:  <https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst>
* PocketSphinx:  <https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst>
* PyAudio: http://people.csail.mit.edu/hubert/pyaudio/docs/
*

