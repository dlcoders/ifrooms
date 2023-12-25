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

        # Generate users
        users = self.generate_users()
        User.objects.bulk_create(users)

        # Generate rooms
        rooms = self.generate_rooms()
        Room.objects.bulk_create(rooms)

        # Generate reservations
        self.generate_reservations(rooms)

        self.stdout.write(self.style.SUCCESS("Fake data loaded successfully!"))

    def generate_rooms(self):
        static_data = [
            {"available": "yes", "department": "main_building", "key": "003", "room_name": "Sala de reuniões"},
            {"available": "yes", "department": "main_building", "key": "027", "room_name": "Auditório"},
            {"available": "yes", "department": "main_building", "key": "056", "room_name": "Laboratório de Informática I"},
            {"available": "yes", "department": "main_building", "key": "057", "room_name": "Laboratório de Informática II"},
            {"available": "yes", "department": "main_building", "key": "058", "room_name": "Laboratório de Informática III"},
            {"available": "yes", "department": "main_building", "key": "060", "room_name": "Laboratório de Redes"},
            {"available": "yes", "department": "main_building", "key": "065", "room_name": "Laboratório de Eletrônica"},
            {"available": "yes", "department": "main_building", "key": "065", "room_name": "Laboratório de Informática IV"},
            {"available": "yes", "department": "main_building", "key": "066", "room_name": "PIBID"},
            { "available": "yes", "department": "laboratories", "key": "078", "room_name": "Laboratorio de Microbiologia"},
            { "available": "yes", "department": "laboratories", "key": "079", "room_name": "Laboratório de Química Orgânica"},
            { "available": "yes", "department": "laboratories", "key": "080", "room_name": "Laboratório de Química Analítica"},
            { "available": "yes", "department": "laboratories", "key": "081", "room_name": "Laboratório Unidade Escola"},
            { "available": "yes", "department": "laboratories", "key": "082", "room_name": "Laboratório de Processamento de Leite e Derivados"},
            { "available": "yes", "department": "laboratories", "key": "083", "room_name": "Laboratório de Química Geral"},
            { "available": "yes", "department": "laboratories", "key": "085", "room_name": "Laboratório de Carnes e Derivados"},
            { "available": "yes", "department": "laboratories", "key": "086", "room_name": "Laboratório de Física"},
            { "available": "yes", "department": "laboratories", "key": "087", "room_name": "Laboratório de Biologia"},
            { "available": "yes", "department": "laboratories", "key": "088", "room_name": "Laboratório Análise de Físico-química de Alimentos"},
            { "available": "yes", "department": "laboratories", "key": "089", "room_name": "Laboratório de Abelhas"},
            { "available": "yes", "department": "laboratories", "key": "090", "room_name": "Laboratório de Processamento de Pólen e Própolis"},
            { "available": "yes", "department": "laboratories", "key": "091", "room_name": "Laboratório Análise de Físico-química de Produtos Apícolas e Geleia Real"},
            { "available": "yes", "department": "honey_house", "key": "097", "room_name": "Recepção e Barreira"},
            { "available": "yes", "department": "honey_house", "key": "098", "room_name": "Rotulagem e Embalagem"},
            { "available": "yes", "department": "apiary", "key": "100", "room_name": "Apiário"},
            { "available": "yes", "department": "classrooms", "key": "109", "room_name": "Sala de Reuniões"},
            { "available": "yes", "department": "main_building", "key": "122", "room_name": "NEABI"},
            { "available": "yes", "department": "classrooms", "key": "122", "room_name": "NUARTE"},
            { "available": "yes", "department": "library", "key": "131", "room_name": "Mini - Auditório"},
            { "available": "yes", "department": "sports_gymnasium", "key": "141", "room_name": "Ginásio"},
            { "available": "yes", "department": "garage", "key": "145", "room_name": "Academia dos Servidores"},
            { "available": "yes", "department": "main_building", "key": "043", "room_name": "Sala de Estudo de Agroindústria"},
        ]

        rooms = []
        for data in static_data:
            room = Room(
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
