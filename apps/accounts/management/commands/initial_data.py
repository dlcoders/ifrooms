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

        # Generate rooms
        rooms = []
        for i in range(10):
            rooms.append(
                Room(
                    room_name=f"Sala {i+1}",
                    key=f"Chave {i+1}",
                    department=random.choice(Room.CHOICES_DEPARTMENT)[0],
                    available=random.choice(Room.STATUS_DEPARTMENT)[0],
                )
            )

        Room.objects.bulk_create(rooms)

        for room in Room.objects.all():
            coordinator = (
                User.objects.filter(registration_type="coordinator")
                .order_by("?")
                .first()
            )
            if coordinator:
                room.id_user_coordinator.add(coordinator)

        # Generate users
        user_type = random.choice(["student", "coordinator", "teacher"])
        users = [
            User(
                registration=fake.unique.random_number(6),
                name=fake.name(),
                email=fake.email(),
                registration_type=user_type,
                is_superuser=fake.boolean(),
                is_staff=fake.boolean(),
                is_active=True,
                is_student=user_type == "student",
                is_coordinator=user_type == "coordinator",
                is_teacher=user_type == "teacher",
            )
            for _ in range(10)
        ]
        User.objects.bulk_create(users)

        # Generate reservations
        for _ in range(10):
            status_choice = random.choice(
                ["Deferido", "Indeferido", "Aguardando Resposta"]
            )

            teachers = User.objects.filter(registration_type="teacher")

            reservation = Reservation(
                date=fake.date_this_decade(),
                startTime=fake.time(),
                endTime=fake.time(),
                justification=random.choice(Reservation.JUSTIFICATION_CHOICES)[0],
                periodicity=random.choice(Reservation.PERIODICITY_CHOICES)[0]
                if fake.boolean()
                else None,
                annex=None,
                message=fake.text(max_nb_chars=150),
                reply=fake.text(max_nb_chars=150),
                status=status_choice,
                id_room=random.choice(rooms),
                id_user_teacher=random.choice(teachers),
            )

            if status_choice in ["Deferido", "Indeferido"] and fake.boolean(
                chance_of_getting_true=50
            ):
                reservation.message = fake.text(max_nb_chars=150)
                reservation.reply = fake.text(max_nb_chars=150)

            reservation.save()

        self.stdout.write(self.style.SUCCESS("Fake data loaded successfully!"))
