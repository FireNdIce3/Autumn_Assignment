from rest_framework.views import APIView
from rest_framework.response import Response
from backend.api.serializers.section_marks import SectionMarksSerializer
from backend.models import Student , Round, InterviewSection, SectionMarks, Interview
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from backend.validation import IsSenior


class InterviewMarksView(APIView):
    permission_classes = [IsAuthenticated, IsSenior]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        student_id = request.GET.get('student_id', None)
        round_id = request.GET.get('round_id', None)
        student = get_object_or_404(Student, id = student_id)
        round = get_object_or_404(Round,id = round_id)
        if round.round_type == 'T':
            return Response({
                "details": "This is not an interview Round"
            }, status=405)
        student_details = {
            "id": student.id,
            "name": student.name,
            "enrolment_number": student.enrolment_number
        }

        round_details = {}
        round_details["round_name"] = round.round_name

        section_details = []
        section_queryset = round.interview_sections.all()
        interview = Interview.objects.get(student = student, round = round)
        for section in section_queryset:
            section_dict = {}
            try:
                section_marks = SectionMarks.objects.get(section = section,
                interview = interview)
            except SectionMarks.DoesNotExist:
                section_marks = None
            section_dict["maximum_marks"] = section.maximum_marks
            section_dict["title"] = section.title
            if section_marks:
                section_dict["section_marks_id"] = section_marks.id
                section_dict["obtained_marks"] = section_marks.obtained_marks
            else:
                section_dict["section_marks_id"] = None
                section_dict["obtained_marks"] = None
            section_details.append(section_dict)
        round_details["sections"] = section_details

        return Response({
            "student_details": student_details,
            "round_details": round_details,
            "interview_remarks": interview.remarks
        })

    def post(self, request):
        request_data = request.data
        if request_data["scores"]:     
            for score in request_data["scores"]:
                if SectionMarks.objects.filter(
                    interview__id = score["interview"],
                    section__id = score["section"]
                    ).count():
                    self.update(request, score)
                else:
                    serialized_data = SectionMarksSerializer(data = score)
                    if serialized_data.is_valid():
                        serialized_data.save()

            return Response({
                "details": "Created Section Marks Instances"
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                "details": "Invalid format for post request."
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, score):
        section_marks_instance = SectionMarks.objects.get(
            interview__id = score["interview"],
            section__id = score["section"]
        )
        serialized_data = SectionMarksSerializer(
            instance = section_marks_instance,
            data = score)
        if serialized_data.is_valid():
            serialized_data.save()
        else:
            return Response(serialized_data.errors,
            status = status.HTTP_400_BAD_REQUEST)