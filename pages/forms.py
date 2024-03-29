# forms.py
from django import forms
from .models import TaskDeliverable

class TaskDeliverableForm(forms.ModelForm):
    class Meta:
        model = TaskDeliverable
        fields = ['DeliverableName', 'DeliverableDescription', 'DeliverableFile', 'Task']

    def __init__(self, *args, **kwargs):
        # Pop 'task_id' from kwargs and set it as an instance variable
        self.task_id = kwargs.pop('task_id', None)
        super(TaskDeliverableForm, self).__init__(*args, **kwargs)

        # Make 'Task' field not required
        self.fields['Task'].required = False

        # If task_id is provided, set the initial value for Task
        if self.task_id:
            self.fields['Task'].initial = self.task_id
            self.fields['Task'].widget.attrs['readonly'] = True

    def clean_Task(self):
        # Validate that Task is not empty if TaskID is provided
        task_id = self.cleaned_data.get('Task')
        if self.task_id and not task_id:
            raise forms.ValidationError("Task is required.")
        return task_id
