from rest_framework import serializers

from classes.models import CLASS_CHOICES
from classes.serializers import ClassSerializer

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    student_classes = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ('id', 'first', 'last', 'email', 'average_gpa', 'student_classes')

    def get_student_classes(self, obj):
        class_dict = dict(CLASS_CHOICES)
        return [{'course': class_dict[c.course], 'grade': c.grade} for c in obj.classes.all()]


class SearchSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, value):
        """
        Make sure there is a max of one space. For only first and last name search
        """
        if len(value.split(' ')) > 2:
            raise serializers.ValidationError("name field can't have more than two spaces")
        return value