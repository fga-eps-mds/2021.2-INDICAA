from api.models import Unidade, Turma, Materia

def delete_everything():
    Turma.objects.all().delete()
    Materia.objects.all().delete()
    Unidade.objects.all().delete()
    
