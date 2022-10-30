from backend.models import Interview
from rest_framework import serializers
from .section_marks import SectionMarksSerializer
from .panel import PanelSerializer

class InterviewSerializer(serializers.ModelSerializer):
    student_details = serializers.SerializerMethodField("get_student_details")
    panel_place = serializers.SerializerMethodField("get_panel_place")

    def get_student_details(self, instance):
        details = {
            "id": instance.student.id,
            "name": instance.student.name,
            "enrolment_number": instance.student.enrolment_number,
            "mobile": instance.student.mobile
        }
        return details
    
    def get_panel_place(self, instance):
        if instance.panel:
            return instance.panel.place
        return None

    class Meta:
        model = Interview
        fields = '__all__'
    
    

# override method validate, such that remarks can be added only by 3or4y.
class InterviewSectionMarksSerializer(serializers.ModelSerializer):
    section_marks = serializers.SerializerMethodField('get_section_details')
    student_details = serializers.SerializerMethodField('get_student_details')

    def get_section_details(self, instance):
        return SectionMarksSerializer(instance.section_marks_set, many = True).data

    def get_student_details(self, instance):
        details = {
            "id": instance.student.id,
            "name": instance.student.name,
            "enrolment_number": instance.student.enrolment_number,
        }
        return details

    class Meta:
        model = Interview
        fields = ['id', 'student_details', 'section_marks', 'remarks']