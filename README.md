## Gabriela Myszkowiak - 120669
## NTPD - LAB 8

# Zadanie 1: Konfiguracja środowiska Apache Airflow

Aby korzystać z Apache Airflow używam Docker Desktop. Konfiguruję Airflow, udaje mi się zalogować UI Airflow.

![image](https://github.com/user-attachments/assets/3646a9bd-1164-4837-ad84-a25092ad020f)


# Zadanie 2: Prosty DAG do re-trenowania modelu

Tworzę prosty kod w Pythonie odpowiedzialny za trening modelu, korzystam z danych Iris. Ustawiam scheduler na 1 dzień. Mój DAG jest widoczny w Airflow


![image](https://github.com/user-attachments/assets/01b4991b-a82a-4b4d-a0e2-99d0648f22e4)


DAG wykonuje się poprawnie, accuracy modelu wyniosło 1


![image](https://github.com/user-attachments/assets/59a494c6-d53c-4ea2-846c-85cc1cc11565)



# Zadanie 3: Rozszerzenie o walidację i warunkowe wymianę modelu

Dodaję walidację do pliku z modelem. Biorąc pod uwagę, że wykorzystałam prosty zbiór Iris, nowa wersja nie mogła przebić wyniku starszej wersji (old_acc = 1), więc zostawiam oryginalny model, a drugi zachowuję jako archiwalny. Zachowuję wersjonowanie modeli.


![image](https://github.com/user-attachments/assets/050ff604-6d78-439c-835d-93b29f2ca238)

