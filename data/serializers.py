from rest_framework import serializers
from .models import Employees


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = '__all__'

    def validate(self, data):
        # username
        if data['username'].islower():
            if 8 <= len(data['username']) <= 20:
                c = 0
                for i in data['username']:
                    if i.isdigit():
                        c += 1
                if c == 0:
                    raise serializers.ValidationError('Username must contain at least one number!!!')
            else:
                raise serializers.ValidationError('Username must be greater than 8 characters!!!')
        else:
            raise serializers.ValidationError('Username must be lowercase character!!!')

        # first_name
        if data['first_name'].isalpha():
            if not data['first_name'][0].isupper():
                raise serializers.ValidationError('First name must begin with upper case!!!')
        else:
            raise serializers.ValidationError('First name must be letter!!!')

        # last_name
        if data['last_name'].isalpha():
            if data['last_name'][0].isupper():
                if not (data['last_name'].endswith('v') or data['last_name'].endswith('a')):
                    raise serializers.ValidationError('Lastname must end with either "v" or "a"!!!')
            else:
                raise serializers.ValidationError('Last name must begin with upper case!!!')
        else:
            raise serializers.ValidationError('Last name must be letter!!!')

        # password
        if 16 > len(data['password']) >= 8:
            c = 0
            for i in data['password']:
                if i.isupper():
                    c += 1
            if c != 0:
                s = 0
                for j in data['password']:
                    if j.isdigit():
                        s += 1
                if s == 0:
                    raise serializers.ValidationError('Password must contain at least one number!!!')
            else:
                raise serializers.ValidationError('Password must contain one uppercase letter!!!')
        else:
            raise serializers.ValidationError('Password length must be greater than 8 and less than 16!!!')

        # phone number
        if data['phone'][1:].isdigit():
            if data['phone'].startswith('+'):
                if 0 < len(data['phone']) < 14:
                    if data['phone'][1:4] == '998':
                        return data
                    else:
                        raise serializers.ValidationError('Phone number must be begin with +998!!!')
                else:
                    raise serializers.ValidationError('Phone number length must be greater than 0 and less than 13!!!')
            else:
                raise serializers.ValidationError('You forgot to enter + at the beginning of the phone number!!!')
        else:
            raise serializers.ValidationError('There is a wrong with phone number. Please check and re-enter!!!')