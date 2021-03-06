from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List

class ItemModelTest(TestCase):
    
    def test_default_text_to_sanity_check_model_is_setup(self):
        item = Item()
        self.assertEqual(item.text, '')
        
        
    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

        
    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
            
            
    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()
            # Note that when we do a item.save, the uniqueness constraint on Item is enforced by the database (not Django as here) and the exception is of type sqlite3.IntegrityError, not ValidationError
            
            
    def test_can_save_same_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='foo')
        item = Item(list=list2, text='foo')
        item.full_clean()   # shouldn't raise ValidationError, since it's in a different list
        
        
    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()), # convert to list so we can compare easily
            [item1, item2, item3]
        )
        
        
    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')
        

class ListModelTest(TestCase):
    
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id,))
        
        
