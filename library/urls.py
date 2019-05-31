from rest_framework import routers
from library.views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'bookcategory', book_category.BookCategoryListAPIView)
router.register(r'books', books.BooksListAPIView)
router.register(r'bookstatus', book_status.BookStatusListAPIView)
router.register(r'bookvendor', book_vendor.BookVendorListAPIView)
router.register(r'cupboard', cupboard.CupBoardListAPIView)

router.register(r'cupboardshelf', cupboard_shelf.CupBoardShelfListAPIView)
router.register(r'issuebook', issuebook.IssueBookListAPIView)
router.register(r'returnrenewbook', return_renew.ReturnRenewBookListAPIView)
router.register(r'fine', fine.FineListAPIView)
router.register(r'cupboardshelffield', cupboardshelf_field.CupboardShelfFieldListAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('list_issuedbooks/', list_issued_books.ListIssuedBooks.as_view()),
    path('cupboardshelfname/', cupboard.GetCupboardshelfname.as_view()),
    

]