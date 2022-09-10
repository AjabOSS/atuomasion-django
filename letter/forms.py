# from . models import Letter
# from django import forms

# class LetterForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(LetterForm, self).__init__(*args, **kwargs)
#         # Making location required
#         self.fields['title'].required = True
#         self.fields['description'].required = True
#         self.fields['target'].required = True
#         self.fields['file'].required = False
#         self.fields['delete_status'].required = True

#     class Meta:
#         model = Letter
#         fields = [
#             "title",
#             "description",
#             "target",
#             "file",
#             "delete_status",
#             ]