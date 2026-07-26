# Py-Password-Generator

One Simple python password generator with interface PyQt5

FIRST CONFIGURATION Space Virtual Envelop separated for developers.

# Install Python3

$ sudo apt install python3     

----- Installing PIP command ------

$ sudo python -m pip install

Create Virtual Space

$ mkdir /home/yourname/git-repo-clone

$ cd git-repo-clone/

$ git clone https://github.com/fabionet/py-password-generator.git

$ cd py-password-generator/

----- Create Envelop Space -----

$ cd home/yourname/git-repo-clone/py-password-generator

- Directory name of default but cat you create with different name in to

$ mkdir venv                                               

$ cd venv

- Installing virtual envelop space

$ python3 -m venv .                                        

$ source bin/activate

$ cd ..

----- Installing PyQt5 Lib -----

$ pip install pyqt5

and.

Execute and develop for this project.

$ python3 passgen.py

Enjoy. ;-)

---

## Security

**v1.1 — Security Fix: Cryptographically Secure Random Number Generator**

Previously, password generation used Python's `random` module (Mersenne Twister PRNG), which is **not suitable for cryptographic purposes**. An attacker observing enough generated output could reconstruct the internal state and predict past/future passwords.

The module has been updated to use Python's built-in `secrets` module, which is backed by the OS CSPRNG (`os.urandom()`), making generated passwords cryptographically secure — as recommended by the [official Python documentation](https://docs.python.org/3/library/secrets.html).