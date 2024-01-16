#  Сервис уведомлений для клиентской рассылки
## Описание проекта

Проект представляет собой бэкенд-часть сервиса уведомлений, спроектированного на базе Django и Django REST Framework. Основной целью проекта является обеспечение эффективного механизма рассылки клиентам.

## Используемые технологии
- python 3.10
- Django 4.2
- DjangoRestFramework  3.14
- Celery 
- Redis
- Postgres
- Swager
- Вспомогательные:
	- Git
	- Docker 
	- Make

## Требования

-  Docker & Docker Compose. [Документация по установке](https://docs.docker.com/engine/install/)
> [! INFO]
> (опционально)
> Для сокращения команды для запуска docker-comose.yml, можно использовать команду ***make up***  - для запуска, ***make down*** - для остановки.  Эти команды нужно использовать в корневой директории (где находиться **Makefile**)
> Однако, у Вас должна быть установлена утилита make.
> 
> [Инструкция по установке утилиты  make](https://linuxhint.com/install-make-ubuntu/)



## Инструкция по запуску.

	1) Зайдите в директорию /scripts запустите скрипт generate_env.sh.
	2) Запустите make up (или sudo docker-compose  -f docker-compose.yml up --build -d  )
	3) Изначально бекенд работает на порту 8000. (порт можно поменять в docker-compsoe.yml)

В итоге, по адресу [localhost:8000/docs](http://localhost:8000/docs) - будет документация по ендпоиинтам в формате OpenAPI (swagger).
Также по адресу [localhost:8000/admin](http://localhost:8000/admin) - откроется встроенная админ панель от Django. 

>[! INFO]
>В случае, если во время генерации env файла, Вы не указали данные для admin user, при запуске приложения, создаcтся дефолтный суперюзер с данными:
>username: **admin**
>password: **admin**



**p.s. Из доп-заданий были выполнены пункты: 3, 5, 6, 8, 9**
В целях конфиденциальности, ссылка на тестовое задание не предоставляется.
