для инициализации бд 
python3 manage.py db init

для того что бы создать новые миграции 
необходиомо в терминале ввести
python3 manage.py db migrate
в папке /migrations/versions/ будет создаcт файл миграции 

для того что бы применить миграции новые миграции
необходиомо в терминале ввести
python3 manage.py db upgrade
бд обновится согласно тем изменениям которые были в /migrations/versions/