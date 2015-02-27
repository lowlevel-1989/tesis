ssh usuario@formatcomtesis.com.ve

if not exist ~/src
	mkdir ~/src

cd ~/src
wget http://bitbucket.org/ianb/virtualenv/get/tip.gz
tar -xvzf tip.gz
rm tip.gz
mv ianb-virtualenv-1f9dfb2437f1/ virtualenv
python virtualenv/virtualenv.py --distribute ~/django/modules
echo 'source ~/django/modules/bin/activate' >> ~/.bash_profile
exit

scp -r ~/Proyectos/tesis/biblioteca usuario@formatcomtesis.com.ve:/home/usuario/django/
ssh usuario@formatcomtesis.com.ve
cd ~/django/biblioteca
pip install -r requirements/production.txt 

biblioteca/settings.py
	line 19: DEBUG = True
	change
	line 19: DEBUG = False
