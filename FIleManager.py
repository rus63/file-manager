print('Добро пожаловать в "Файловый менеджер"!')

   
def begin():
   print('Список доступных команд:\n/create - Создать новый файл\n/delete - Удалить файл\n/change - Изменить файл\n/rename - Переименовать файл\n/exit - Выход\n')
   global comand
   actions=['/create','/delete','/change','/rename','/exit']
   comand=input("Введите команду: ")
   if comand not in actions:
      begin()



def create():
   name=input('Введите название файла: ')
   format=input('Введите формат файла: ')
   f=open(f'{name}.{format}','w')
   f.close()
   print()
   print(f'[INFO] Файл "{name}.{format}" успешно создан!')
   print()
   begin()

def delete():
   name=input('Введите название файла: ')
   from os import remove
   try:
      remove('{}'.format(name))
      print('[INFO] Файл "{}" успешно удален!'.format(name))
   except Exception: 
      print('[ERROR] Файл "{}" не найден!'.format(name))
   finally:
      print()   
      begin()
      
def rename():
   from os import rename
   old_name=input('Введите старое название файла: ')
   new_name=input('Введите новое название файла: ')
   try:
      rename(old_name, new_name)
      print('[INFO] Файл успешно переименован!')
   except Exception:
      print('[ERROR] Файл не найден!')
   finally:
      print()   
      begin()

def change():
   file_name=input('Введите название файла: ')
   try:
      f=open(f'{file_name}')
      print('Как вы хотите изменить ваш файл?\n1) Записать данные в файл\n2) Перезаписать данные в файле\n3) Удалить данные из файла')
      def choise():
         variant=input('Ваш выбор: ')
         variants=['1','2','3']
         if variant not in variants:
            choise()
      choise()
      
   except Exception:
      print('[ERROR] Файл не найден!')
   finally:
      print()   
      begin()
def exit():
   print()
   print('Good bye!')
   print()



def manage():
   if comand!='/exit':
      if comand=='/create':
         create()
      elif comand=='/exit':
         exit()
      elif comand=='/delete':
         delete()
      elif comand=='/rename':
         rename()
      elif comand=='/change':
         change()
      
      manage()
   else:
      exit()
      
   
begin()
manage()

















