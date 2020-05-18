from django import forms
from .models import Book
import datetime

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publishdate','pages','booktype')
        labels = {
            'title':'Title of Book',
            'author': 'Author',
            'publishdate': 'Published Date (YYYY-MM-DD)',
            'pages':'Number of Pages',
            'booktype':'Type of Book'
        }

    
    def __init__(self,*args,**kwargs):
        super(BookForm, self).__init__(*args,**kwargs)
        self.fields['booktype'].empty_label = "Select"
        self.fields['publishdate'].required = False
        self.fields['pages'].required = False
        self.fields['booktype'].required = False

