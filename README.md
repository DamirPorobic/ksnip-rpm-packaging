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
## Adding a new version
We assume that the Repo was downloaded as explained in "Creating a Package from existing release".
In order to create a new version, we need first the source .tar.gz file for this new version. We are downloading the version 1.4.0,  please replace this number with the correct version:
```
dporobic@linux:~/projects/$ wget https://github.com/DamirPorobic/ksnip/archive/v1.4.0.tar.gz
```
Now lets move the downloaded file to the correct directory and rename it at the same time:
```
dporobic@linux:~/projects/$ mv v1.4.0.tar.gz ksnip-rpm-packaging/SOURCES/ksnip-1.4.0.tar.gz
```
Copy the spec file of the previous version and rename it to reflect the correct version:
```
dporobic@linux:~/projects/$ cd ksnip-rpm-packaging/SPECS/
dporobic@linux:~/projects/ksnip-rpm-packaging/SPECS/$ cp ksnip-1.3.2.spec ksnip-1.4.0.spec
```
Now update the new spec file to reflect the new release, at least the version and changelog need to be updated, eventually
other fields too. After this was done, you can proceed with building the rpm like explained in the "Creating a Package from existing release" section.
