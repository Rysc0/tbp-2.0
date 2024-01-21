# APlikacija za temporalno mjerenje i obračun troškova rada

### Upute za instalaciju

Potrebno je imati instalirano sljedeće:
- Python 3.8.10 ili novije
- psycopg2
- tkinter
- tkcalendar
- PostgreSQL 16.1

U skripti db_execute_script.py promijeniti varijablu "sql_script_path" i postaviti path na datoteku "create.sql".
Pod pretpostavkom da je postgres instaliran pokrenuti skriptu: 
- db_create.py

Nakon nje pokrenuti: 
- db_execute_script.py

*Ako se skripte ne izvrše uspješno možda je potrebno promijeniti postavke za spajanje na bazu, najvjerovatnije lozinku za postgres user-a.

Nakon uspješnog kreiranja baze podataka aplikacija se pokreće izvršavanjem skripte 
- app.py