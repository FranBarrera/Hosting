<VirtualHost *:80>
	ServerAdmin user_name@{{domain}}
	ServerName mysql.{{domain}}

	DocumentRoot /usr/share/phpmyadmin/

	<Directory /usr/share/phpmyadmin/>
			Options Indexes FollowSymLinks MultiViews
			AllowOverride None
			Order allow,deny
			allow from all
	</Directory>
</VirtualHost>