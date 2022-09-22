Ogni file .pickle nella directory Utenti salva un "profilo" sotto forma di dizionario.
Provando a scrivere il dizionario su normale file txt col metodo write trasformava
l'oggetto in una stringa.

Studente:
{key:value} --> {codice fiscale: oggetto Studente}
Docente:
{key:value} --> {codice fiscale: oggetto Docente}
Admin:
{key:value} --> {username: oggetto Admin}