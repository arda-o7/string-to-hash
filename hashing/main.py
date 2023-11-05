import hashlib
from colorama import Fore


print(Fore.BLACK + ("Free Hashing"))

yapilacak_islem = input("Yapmak İstediğiniz İşlemi Giriniz: (örnek: encode, decode): ")


if yapilacak_islem == "encode":

    karakter = input("String Giriniz: ")

    hash_sec = input("Hangi Hash Encryptini Kullanmak İstersiniz: (Örnek: md5, sha1, sha256, sha224, sha512, sha384): ")

    if hash_sec == "md5":
        hashjob = hashlib.md5()
        hashjob.update(karakter.encode())
        print(Fore.GREEN + (hashjob.hexdigest()))

    elif hash_sec == "sha1":
        hashjob = hashlib.sha1()
        hashjob.update(karakter.encode())
        print(Fore.GREEN + (hashjob.hexdigest()))

    elif hash_sec == "sha256":
        hashjob = hashlib.sha256()
        hashjob.update(karakter.encode())
        print(Fore.GREEN + (hashjob.hexdigest()))

    elif hash_sec == "sha224":
        hashjob = hashlib.sha224()
        hashjob.update(karakter.encode())
        print(Fore.GREEN + (hashjob.hexdigest()))

    elif hash_sec == "sha512":
        hashjob = hashlib.sha512()
        hashjob.update(karakter.encode())
        print(Fore.GREEN + (hashjob.hexdigest()))

    elif hash_sec == "sha384":
        hashjob = hashlib.sha384()
        hashjob.update(karakter.encode())
        print(Fore.GREEN + (hashjob.hexdigest()))

    else:
        print("Eksik Veya Hatalı Giriş Yaptınız Lütfen Tekrar Deneyiniz!")

else:
    print("Lutfen 'encode' veya 'decode' giriniz.")