# x-mint-layout
Layout Manager for ubuntu based System with XFCE Desktop


erstellen eines .deb installationspaketes

abhängigkeiten: git

git installieren: sudo apt install git

mit folgendem befehl:<br>
git clone "https://github.com/VerEnderT/x-mint-layout.git" x-mint-layout && rm -rf ./x-mint-layout/.git/ && chmod +x ./x-mint-layout/usr/bin/x-mint-layout && dpkg-deb --build x-mint-layout && rm -rf x-mint-layout/

.deb paket installieren:
sudo apt install ./x-mint-layout.deb

