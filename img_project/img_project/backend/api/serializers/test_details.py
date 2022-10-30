from rest_framework import serializers
from backend.models import Test, Marks
from .section import SectionWithQuestionSerializer


class TeststudentSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField("get_test_students")

    def get_test_students(self, instance):
        number_of_questions = 0
        section_list = instance.section_set.all()
        for section in section_list:
            number_of_questions += section.question_set.count()
        student_list = []
        search_params = self.context["request"].query_params.get(
            "search", None)
        evaluated_params = self.context["request"].query_params.get(
            "evaluated", None
        )
        min_marks_params = self.context["request"].query_params.get(
            "min_marks", None
        )
        max_marks_params = self.context["request"].query_params.get(
            "max_marks", None
        )

        for test_student in instance.round.students.all():
            if not search_params or test_student.name.lower().find(search_params.lower()) != -1 or str(test_student.enrolment_number).find(search_params) != -1:
                student_dict = {}
                student_dict["id"] = test_student.id
                student_dict["name"] = test_student.name
                student_dict["enrolment_number"] = test_student.enrolment_number
                student_dict["mobile"] = test_student.mobile
                total_marks = 0
                for score in Marks.objects.filter(
                    student=test_student,
                    question__section__test=instance
                ):
                    total_marks += score.obtained_marks
                if number_of_questions != Marks.objects.filter(
                        student=test_student,
                        question__section__test=instance).count():
                    student_dict["status"] = "Not Evaluated"
                else:
                    student_dict["status"] = "Evaluated"

                print(self.context.get("is3yor4y"))
                if (not evaluated_params or (evaluated_params == "true" and student_dict["status"] == "Evaluated") or (evaluated_params == "false" and student_dict["status"] == "Not Evaluated")):
                    if (not min_marks_params or not self.context.get("is3yor4y") or (int(min_marks_params) <= total_marks)):
                        if (not max_marks_params or not self.context.get("is3yor4y") or (int(max_marks_params) >= total_marks)):
                            student_list.append(student_dict)
        return student_list

    class Meta:
        model = Test
        fields = ['id', 'title', 'students']


class TestSectionSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField("get_sections_with_questions")

    def get_sections_with_questions(self, instance):
        section_queryset = instance.section_set
        return SectionWithQuestionSerializer(section_queryset, many=True).data

    class Meta:
        model = Test
        fields = ['id', 'title', 'sections']
