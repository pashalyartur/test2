from django.shortcuts import render, redirect
from .models import Test, Result, CorrectAnswer
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Test, Result


def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_autor/test_list.html', {'tests': tests})


def test_detail(request, test_id):
    test = Test.objects.get(pk=test_id)
    return render(request, 'test_autor/test_detail.html', {'test': test})


def submit_test(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(pk=test_id)
        questions = test.question_set.all()
        score = 0

        for question in questions:
            selected_answers = request.POST.getlist(f'question_{question.id}')
            correct_answers = CorrectAnswer.objects.filter(question=question)

            if set(selected_answers) == set(correct_answers.values_list('answer__answer_text', flat=True)):
                score += 1

        result = Result(test=test, student_name=request.POST.get('student_name'), score=score)
        result.save()

        return redirect('test_result', result_id=result.id)
    else:
        return redirect('test_list')

def test_result(request, result_id):
    result = Result.objects.get(pk=result_id)
    return render(request, 'test_autor/test_result.html', {'result': result})

def teacher(request):
    tests = Test.objects.all()
    return render(request, 'test_autor/test_list_teacher.html', {'tests': tests})

def infa(request, test_id):
    test = Test.objects.get(pk=test_id)
    results = Result.objects.filter(test=test)
    return render(request, 'test_autor/infa.html', {'test': test, 'results': results})



def generate_test_results_html(request, test_id):
    test = Test.objects.get(pk=test_id)
    results = Result.objects.filter(test=test)
    html = render_to_string('test_autor/teacher.html', {'test': test, 'results': results})
    
    response = HttpResponse(content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="{test.title}_results.html"'
    response.write(html)
    
    return response