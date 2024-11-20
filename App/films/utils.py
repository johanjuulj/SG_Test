from django.db.models import Max
from films.models import UserTasks

def get_max_order(user) -> int:
    existing_tasks = UserTasks.objects.filter(user=user)
    if not existing_tasks.exists():
        return 1
    else:
        current_max = existing_tasks.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1
    

def reorder(user):
    existing_tasks = UserTasks.objects.filter(user=user)    
    if not existing_tasks.exists():
        return
    number_of_tasks = existing_tasks.count()
    new_ordering = range (1, number_of_tasks + 1)
    for order, user_tasks in zip(new_ordering, existing_tasks):
        user_tasks.order = order
        user_tasks.save()