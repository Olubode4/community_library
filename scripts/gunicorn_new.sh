#!/usr/bin/bash
#sudo cp /home/ubuntu/locallibrary/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
#sudo cp /home/ubuntu/locallibrary/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

#sudo systemctl start gunicorn.service
#sudo systemctl enable gunicorn.service

sudo cp /home/ubuntu/locallibrary/gunicorn/gunicorn.conf  /etc/supervisor/conf.d/gunicorn.conf

sudo mkdir /var/log/gunicorn
sudo supervisorctl reread
sudo supervisorctl update

# check the status of gunicorn
sudo supervisorctl status

sudo supervisorctl restart guni:gunicorn