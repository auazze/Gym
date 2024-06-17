from django.contrib.auth.models import User

# Проверка существования суперпользователя
superusers = User.objects.filter(is_superuser=True)
print(superusers)

# Изменение пароля суперпользователя
if superusers.exists():
    user = superusers.first()
    user.set_password('auazze')
    user.save()
else:
    # Создание нового суперпользователя
    User.objects.create_superuser('auazze', '', 'auazze')
