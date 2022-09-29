from rest_framework import serializers
from .models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('fName', 'lName', 'email','phone','imageUrl')
