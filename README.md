# GitHub User Activity Tracker

Questo progetto consente di recuperare e visualizzare l'attività pubblica di un utente GitHub. È realizzato in Python e utilizza l'API di GitHub per ottenere gli eventi pubblici dell'utente.
Qui potete trovare i dettagli sull esercitazione: https://roadmap.sh/projects/github-user-activity

## Funzionalità
- Recupera gli eventi pubblici di un utente su GitHub.
- Analizza e visualizza l'attività dell'utente, inclusi tipi di eventi e repository coinvolti.
- Utilizza `argparse` per passare l'username come argomento da terminale.

## Requisiti
- Python 3.x
- `requests` (installabile tramite `pip`)

## Installazione

1. Clona questo repository:
    ```sh
    git clone https://github.com/tuo-utente/github-user-activity.git
    cd github-user-activity
    ```

2. Installa la libreria `requests`:
    ```sh
    pip install requests
    ```

## Uso

Per eseguire lo script e visualizzare l'attività di un utente, usa il seguente comando nel terminale:

```sh
python github_activity.py <username>
