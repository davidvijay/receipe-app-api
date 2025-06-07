"""
Django commands to wait for db to available

"""
import time
from psycopg2 import OperationalError as pyscopg2OpError # noqa
from django.db.utils import OperationalError 
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""
    def handle(self, *args, **options):
        """Entry point of command"""
        self.stdout.write("Hello")
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.stdout.write("In try")
                self.check(databases=["default"])
                db_up = True
            except OperationalError:
                self.stdout.write("In except")
                self.stdout.write("Database unavailable, Waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
