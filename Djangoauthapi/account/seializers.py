from rest_framework import serializers
from account.models import User

class UserRegistraionsSerializers(serializers.ModelSerializer):

  # We are writing this becoz we need confirm password field in our Registratin Request
    # password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['email', 'name', 'password',  'tc']
        extra_kwargs={
        'password':{'write_only':True}
        }

        # Validate
        def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password2 is doesn't match!!")
            return attrs
        
        def create(self, validate_data):
            # Remove password2 from validated_data as it's not needed in the User model
            # validated_data.pop('password2')
            # Now create the user with the remaining data
            # password = validate_data.pop('password')
            # validate_data.pop('password2') 
            user = User.objects.create_user(**validate_data)
            return user
        
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']

class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={'input' : 'pssword'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input' : 'pssword'}, write_only=True)

    class Meta:
       
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Doesn't Match")
        user.set_password(password)
        user.save()
        return attrs