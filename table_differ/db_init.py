__author__ = 'ajboehmler'

import models

models.User.create_table()

admin = models.User(username='admin',
                    email='admin@example.com',
                    admin=True,
                    active=True)
admin.set_password('admin')
admin.save()