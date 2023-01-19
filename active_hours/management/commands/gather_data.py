from django.core.management.base import BaseCommand
from environs import Env
from active_hours.management.commands.linkedin_api import login
from bs4 import BeautifulSoup
from active_hours.models import Contact, Presence
from django.utils import timezone


class Command(BaseCommand):

    def handle(self, *args, **options):
        env = Env()
        env.read_env()

        email = env('LINKEDIN_LOGIN')
        password = env('LINKEDIN_PASSWORD')
        connections = login(email=email, password=password)

        with open('file_for_parsing.txt', 'r', encoding='utf-8') as file:
            connections = file.read()

        soup = BeautifulSoup(connections, 'lxml')

        lis = soup.find_all('li')
        for li in lis:
            presence = li.find(
                class_='presence-entity presence-entity--size-5').span.text.strip().replace('\n', '')
            name = li.find(
                class_='mn-connection-card__name t-16 t-black t-bold').text.strip().replace('\n', '')
            occupation = li.find(
                class_='mn-connection-card__occupation t-14 t-black--light t-normal').text.strip().replace('\n', '')

            member, _ = Contact.objects.get_or_create(
                full_name=name,
                defaults={
                    'occupation': occupation,
                }
            )
            Presence.objects.get_or_create(
                current_time=timezone.now(),
                contact=member,
                status=presence,
            )
