# ksnip-rpm-packaging

Repository for creating .rpm binaries for [ksnip](https://github.com/DamirPorobic/ksnip)

## Creating a Package from existing release
First step is getting the Repo from GitHub, run following command from a directory where you would like to create the package:
```
dporobic@linux:~/projects/$ git clone https://github.com/DamirPorobic/ksnip-rpm-packaging.git
```
Switch to the repository directory: 
```
dporobic@linux:~/projects/$ cd ksnip-rpm-packaging/
dporobic@linux:~/projects/ksnip-rpm-packaging/$
```
Now run the rpmbuild command with the spec file of the version that you want to build, in this case it's the version 1.4.0:
```
dporobic@linux:~/projects/ksnip-rpm-packaging/$ rpmbuild -ba SPECS/ksnip-1.4.0.spec --define '_topdir %(pwd)'
```
If you want to sign the package while building, you first need to create a gpg key and then add following two entries to the `~/.rpmmacros` file, where "Ksnip" is the name of the gpg key:
```
dporobic@linux:~/projects/ksnip-rpm-packaging/$ echo %_signature gpg >> ~/.rpmmacros && echo %_gpg_name Ksnip >> ~/.rpmmacros
```
Now you can build the rpm and sign the package at the same time:
```
dporobic@linux:~/projects/ksnip-rpm-packaging/$ rpmbuild -ba --sign SPECS/ksnip-1.4.0.spec --define '_topdir %(pwd)'
```



