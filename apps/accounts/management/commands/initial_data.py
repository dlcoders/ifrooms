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
        static_data = [
            {"id": 1, "available": "yes", "department": "main_building", "key": "003", "room_name": "Sala de reuniões"},
            {"id": 2, "available": "yes", "department": "main_building", "key": "027", "room_name": "Auditório"},
            {"id": 3, "available": "yes", "department": "main_building", "key": "056", "room_name": "Laboratório de Informática I"},
            {"id": 4, "available": "yes", "department": "main_building", "key": "057", "room_name": "Laboratório de Informática II"},
            {"id": 5, "available": "yes", "department": "main_building", "key": "058", "room_name": "Laboratório de Informática III"},
            {"id": 6, "available": "yes", "department": "main_building", "key": "060", "room_name": "Laboratório de Redes"},
            {"id": 7, "available": "yes", "department": "main_building", "key": "065", "room_name": "Laboratório de Eletrônica"},
            {"id": 8, "available": "yes", "department": "main_building", "key": "065", "room_name": "Laboratório de Informática IV"},
            {"id": 9, "available": "yes", "department": "main_building", "key": "066", "room_name": "PIBID"},
            {"id": 10, "available": "yes", "department": "laboratories", "key": "078", "room_name": "Laboratorio de Microbiologia"},
            {"id": 11, "available": "yes", "department": "laboratories", "key": "079", "room_name": "Laboratório de Química Orgânica"},
            {"id": 12, "available": "yes", "department": "laboratories", "key": "080", "room_name": "Laboratório de Química Analítica"},
            {"id": 13, "available": "yes", "department": "laboratories", "key": "081", "room_name": "Laboratório Unidade Escola"},
            {"id": 14, "available": "yes", "department": "laboratories", "key": "082", "room_name": "Laboratório de Processamento de Leite e Derivados"},
            {"id": 15, "available": "yes", "department": "laboratories", "key": "083", "room_name": "Laboratório de Química Geral"},
            {"id": 16, "available": "yes", "department": "laboratories", "key": "085", "room_name": "Laboratório de Carnes e Derivados"},
            {"id": 17, "available": "yes", "department": "laboratories", "key": "086", "room_name": "Laboratório de Física"},
            {"id": 18, "available": "yes", "department": "laboratories", "key": "087", "room_name": "Laboratório de Biologia"},
            {"id": 19, "available": "yes", "department": "laboratories", "key": "088", "room_name": "Laboratório Análise de Físico-química de Alimentos"},
            {"id": 20, "available": "yes", "department": "laboratories", "key": "089", "room_name": "Laboratório de Abelhas"},
            {"id": 21, "available": "yes", "department": "laboratories", "key": "090", "room_name": "Laboratório de Processamento de Pólen e Própolis"},
            {"id": 22, "available": "yes", "department": "laboratories", "key": "091", "room_name": "Laboratório Análise de Físico-química de Produtos Apícolas e Geleia Real"},
            {"id": 23, "available": "yes", "department": "honey_house", "key": "097", "room_name": "Recepção e Barreira"},
            {"id": 24, "available": "yes", "department": "honey_house", "key": "098", "room_name": "Rotulagem e Embalagem"},
            {"id": 25, "available": "yes", "department": "apiary", "key": "100", "room_name": "Apiário"},
            {"id": 26, "available": "yes", "department": "classrooms", "key": "109", "room_name": "Sala de Reuniões"},
            {"id": 27, "available": "yes", "department": "main_building", "key": "122", "room_name": "NEABI"},
            {"id": 28, "available": "yes", "department": "classrooms", "key": "122", "room_name": "NUARTE"},
            {"id": 29, "available": "yes", "department": "library", "key": "131", "room_name": "Mini - Auditório"},
            {"id": 30, "available": "yes", "department": "sports_gymnasium", "key": "141", "room_name": "Ginásio"},
            {"id": 31, "available": "yes", "department": "garage", "key": "145", "room_name": "Academia dos Servidores"},
            {"id": 32, "available": "yes", "department": "main_building", "key": "043", "room_name": "Sala de Estudo de Agroindústria"},
        ]

        rooms = []
        for data in static_data:
            room = Room(
                id=data["id"],
                available=data["available"],
                department=data["department"],
                key=data["key"],
                room_name=data["room_name"],
            )
            rooms.append(room)

        return rooms

    def generate_users(self):
        user_type = random.choice(["student", "teacher"])
        users = []

        if user_type == "teacher":
            users.append(
                User(
                    registration=self.fake.unique.random_number(6),
                    name=self.fake.name(),
                    email=self.fake.email(),
                    registration_type=user_type,
                    is_superuser=self.fake.boolean(),
                    is_staff=self.fake.boolean(),
                    is_active=True,
                    is_student=False,
                    is_teacher=True,
                )
            )

        users.extend([
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
            for _ in range(9)
        ])

        return users

    def generate_reservations(self, rooms):
        for _ in range(10):
            status_choice = random.choice(["Deferido", "Indeferido", "Aguardando Resposta"])
            teachers = User.objects.filter(registration_type="teacher")

            reservation = Reservation(
                date=self.fake.date_this_decade(),
                start_time=self.fake.time(),
                end_time=self.fake.time(),
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
