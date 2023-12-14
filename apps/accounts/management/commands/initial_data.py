from django.core.management.base import BaseCommand
from apps.accounts.models import User
from apps.reservation.models import Reservation
from apps.rooms.models import Room
from faker import Faker
import random


class Command(BaseCommand):
    help = "Load a large set of initial data into the database"

    def handle(self, *args, **kwargs):
        fake = Faker("pt_BR")
        self.fake = fake

        # Generate rooms
        rooms = self.generate_rooms()
        Room.objects.bulk_create(rooms)

        # Generate users
        users = self.generate_users()
        User.objects.bulk_create(users)

        # Generate reservations
        self.generate_reservations(rooms)

        self.stdout.write(self.style.SUCCESS("Fake data loaded successfully!"))

    def generate_rooms(self):
        rooms = []
        for i in range(10):
            room = Room(
                room_name=f"Sala {i + 1}",
                key=f"Chave {i + 1}",
                department=random.choice(Room.CHOICES_DEPARTMENT)[0],
                available=random.choice(Room.STATUS_DEPARTMENT)[0],
            )
            rooms.append(room)

        return rooms

    def generate_users(self):
        user_type = random.choice(["student", "teacher"])
        users = [
            User(
                registration=self.fake.unique.random_number(6),
                name=self.fake.name(),
                email=self.fake.email(),
                registration_type=user_type,
                is_superuser=self.fake.boolean(),
                is_staff=self.fake.boolean(),
                is_active=True,
                is_student=user_type == "student",
                is_teacher=user_type == "teacher",
            )
            for _ in range(10)
        ]

        return users

    def generate_reservations(self, rooms):
        for _ in range(10):
            status_choice = random.choice(["Deferido", "Indeferido", "Aguardando Resposta"])
            teachers = User.objects.filter(registration_type="teacher")

            reservation = Reservation(
                date=self.fake.date_this_decade(),
                startTime=self.fake.time(),
                endTime=self.fake.time(),
                justification=self.fake.text(max_nb_chars=200),
                periodicity=random.choice(Reservation.PERIODICITY_CHOICES)[0] if self.fake.boolean() else None,
                annex=None,
                message=self.fake.text(max_nb_chars=150),
                reply=self.fake.text(max_nb_chars=150),
                status=status_choice,
                id_room=random.choice(rooms),
                id_user_teacher=random.choice(teachers),
            )

            if status_choice in ["Deferido", "Indeferido"] and self.fake.boolean(chance_of_getting_true=50):
                reservation.message = self.fake.text(max_nb_chars=150)
                reservation.reply = self.fake.text(max_nb_chars=150)

            reservation.save()
