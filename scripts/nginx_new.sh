
#!/usr/bin/bash

#sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

#sudo cp /home/ubuntu/locallibrary/nginx/nginx.conf /etc/nginx/sites-available/locallibrary
sudo cp /home/ubuntu/locallibrary/nginx/nginx_new.conf /etc/nginx/sites-available/django.conf
#sudo ln -s /etc/nginx/sites-available/locallibrary /etc/nginx/sites-enabled/
sudo ln /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
#sudo systemctl restart nginx

#sudo service nginx start
sudo service nginx reload
#sudo service nginx restart
# restart nginx
sudo systemctl restart nginx
