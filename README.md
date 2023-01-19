# LinkedIn parser of presence statuses

Parser is designed to help you understand when your contacts are present during the day.

## How to launch locally

- Download code  
```git clone https://github.com/tbaiguzhinov/linkedin_parser```
- Go to the folder  
```cd linkedin_parser```
- Set up virtual environment  
```virtualenv venv```
- Install dependencies  
```pip3 install -r requirements.txt```
- Launch code  
```python3 manage.py gather_data```

## Cron jobs

It is recomended to set up a cronjob for this script as per the frequency you need:  
```bash
*/20 * * * * /home/linkedin_parser/venv/bin/python3.7 /home/linkedin_parser/manage.py gather_data >> /home/logs.txt 2>&1
```
Adding this line to crontab will launch script from linkedin_parser every 20 minutes.

## Environment variables

For your code to work, you need to add your credentials to environment variabls. Create a file `.env` next to `manage.py` and add varilables in the following format: `VARIABLE=value`.

* `LINKEDIN_LOGIN` - Your email which you use to log into LinkedIn.
* `LINKEDIN_PASSWORD` - Your LinkedIn password.

## Project aims

To understand when your connections are online.
